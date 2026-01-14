#!/usr/bin/env python3
import argparse
import json
import os
import random
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

import img2pdf
from PIL import Image
from pypdf import PdfReader, PdfWriter
from pagelabels import PageLabelScheme, PageLabels
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import JavascriptException
from seleniumwire import webdriver as wire_webdriver
from tqdm import tqdm

from fucts.roman import move_romans_to_front, roman_sort_with_ints, try_convert_int


def random_delay(base_delay, variance=0.5):
    """Generate a random delay with variance to appear more human-like"""
    min_delay = base_delay * (1 - variance)
    max_delay = base_delay * (1 + variance)
    delay = random.uniform(min_delay, max_delay)
    return delay


def human_like_delay(min_delay=2, max_delay=5):
    """Generate a human-like delay with occasional longer pauses"""
    # 80% of the time use normal delay
    # 20% of the time use a longer delay (simulating user distraction)
    if random.random() < 0.8:
        return random.uniform(min_delay, max_delay)
    else:
        return random.uniform(max_delay, max_delay * 2)


def simulate_human_behavior(driver):
    """Simulate random human-like behavior"""
    actions = ActionChains(driver)
    
    # Randomly perform one of several actions
    behavior = random.choice(['scroll', 'mouse_move', 'pause', 'none'])
    
    if behavior == 'scroll':
        # Random small scroll
        scroll_amount = random.randint(-100, 100)
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
    elif behavior == 'mouse_move':
        # Random mouse movement
        try:
            x_offset = random.randint(-50, 50)
            y_offset = random.randint(-50, 50)
            actions.move_by_offset(x_offset, y_offset).perform()
        except:
            pass
    elif behavior == 'pause':
        # Just a longer pause
        time.sleep(random.uniform(0.5, 2))


parser = argparse.ArgumentParser()
parser.add_argument('--output', default='./output/')
parser.add_argument('--yuzu', default=False, action='store_true')
parser.add_argument('--isbn', required=True)
parser.add_argument('--delay', default=3, type=int, help='Base delay between pages (will be randomized)')
parser.add_argument('--delay-variance', default=0.5, type=float, help='Variance for delays (0.5 = ±50%)')
parser.add_argument('--min-delay', default=2, type=int, help='Minimum delay between actions')
parser.add_argument('--max-delay', default=6, type=int, help='Maximum delay between actions')
parser.add_argument('--pages', default=None, type=int, help='Override how many pages to save.')
parser.add_argument('--start-page', default=0, type=int, help='Start on this page.')
parser.add_argument('--end-page', default=-1, type=int, help='End on this page.')
parser.add_argument('--chrome-exe', default=None, type=str, help='Path to the Chrome executable.')
parser.add_argument('--disable-web-security', action='store_true', help="Disable CORS protections.")
parser.add_argument('--language', default='eng', help='OCR language. Default: "eng"')
parser.add_argument('--skip-scrape', action='store_true', help="Don't scrape, just rebuild PDF.")
parser.add_argument('--only-scrape-metadata', action='store_true', help="Only scrape metadata.")
parser.add_argument('--skip-ocr', action='store_true', help="Don't do OCR.")
parser.add_argument('--compress', action='store_true', help="Compress and optimize PDF.")
parser.add_argument('--stealth-mode', default=True, action='store_true', help="Enable stealth mode (anti-detection)")
parser.add_argument('--user-agent', default=None, type=str, help='Custom user agent string')
args = parser.parse_args()

args.output = Path(args.output)
args.output.mkdir(exist_ok=True, parents=True)
ebook_files = args.output / args.isbn
ebook_files.mkdir(exist_ok=True, parents=True)

book_info = {}
non_number_pages = 0

platform_identifiers = {
    'home_url': "https://reader.yuzu.com",
    'jigsaw_url': "https://jigsaw.yuzu.com",
    'total_pages_css': ".sc-wkwDy.ebHWgB",
    'current_page_css': ".InputControl__input-fbzQBk.hDtUvs",
    'page_loader_css': ".sc-hiwPVj.hZlgDU",
    'next_page_css': ".IconButton__button-bQttMI.cSDGGI",
} if args.yuzu else {
    'home_url': "https://bookshelf.vitalsource.com",
    'jigsaw_url': "https://jigsaw.vitalsource.com",
    'total_pages_css': ".sc-wkwDy.ebHWgB",
    'current_page_css': ".InputControl__input-fbzQBk.hDtUvs",
    'page_loader_css': ".sc-AjmGg.dDNaMw",
    'next_page_css': ".IconButton__button-bQttMI.cSDGGI",
}


def get_num_pages():
    retry_count = 0
    max_retries = 10
    
    while retry_count < max_retries:
        try:
            total_text = driver.execute_script(
                'return document.querySelector("' + 
                platform_identifiers['total_pages_css'] + '").innerHTML'
            ).strip()
            
            if '/' in total_text:
                total = int(total_text.split('/')[-1].strip())
            else:
                total = int(total_text.strip())
            
            try:
                current_page = driver.execute_script(
                    'return document.querySelector("' + 
                    platform_identifiers['current_page_css'] + '").value'
                )
                if current_page == '' or not current_page:
                    current_page = 0
            except JavascriptException:
                current_page = 0
            return current_page, total
        except (JavascriptException, TypeError, AttributeError) as e:
            retry_count += 1
            wait_time = random_delay(1, 0.3)
            print(f"Waiting for page elements ({retry_count}/{max_retries})... {wait_time:.2f}s")
            time.sleep(wait_time)
    
    raise Exception("Failed to get page numbers after maximum retries")


def load_book_page(page_id):
    driver.get(f"{platform_identifiers['home_url']}/reader/books/{args.isbn}/pageid/{page_id}")
    time.sleep(random_delay(2, 0.5))
    get_num_pages()
    
    # Wait for page loader to disappear with random delays
    wait_count = 0
    while len(driver.find_elements(By.CSS_SELECTOR, platform_identifiers['page_loader_css'])):
        time.sleep(random_delay(1, 0.3))
        wait_count += 1
        if wait_count > 30:
            print("Warning: Page loader taking unusually long...")
            break


if not args.skip_scrape or args.only_scrape_metadata:
    chrome_options = webdriver.ChromeOptions()
    
    # Stealth mode options
    if args.stealth_mode:
        # Anti-detection measures
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        
        # Random user agent if not specified
        if args.user_agent:
            chrome_options.add_argument(f'user-agent={args.user_agent}')
        else:
            user_agents = [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            ]
            chrome_options.add_argument(f'user-agent={random.choice(user_agents)}')
    
    if args.disable_web_security:
        chrome_options.add_argument('--disable-web-security')
        print('DISABLED WEB SECURITY!')
    
    chrome_options.add_argument('--disable-http2')
    
    if args.chrome_exe:
        chrome_options.binary_location = args.chrome_exe
    
    seleniumwire_options = {
        'disable_encoding': True
    }
    
    # Find chromedriver
    chromedriver_path = shutil.which('chromedriver')
    if chromedriver_path:
        service = Service(chromedriver_path)
    else:
        common_paths = [
            '/usr/bin/chromedriver',
            '/usr/local/bin/chromedriver',
            '/usr/lib/chromium/chromedriver',
        ]
        service = None
        for path in common_paths:
            if os.path.exists(path):
                service = Service(path)
                print(f'Using chromedriver from: {path}')
                break
        if not service:
            print("ERROR: Could not find chromedriver. Please install it:")
            print("  sudo apt install chromium-driver")
            exit(1)
    
    driver = wire_webdriver.Chrome(
        service=service,
        options=chrome_options, 
        seleniumwire_options=seleniumwire_options
    )
    
    # Additional stealth measures
    if args.stealth_mode:
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": driver.execute_script("return navigator.userAgent").replace('Headless', '')
        })

    driver.get(platform_identifiers['home_url'])
    input('Press ENTER once logged in...')

    driver.maximize_window()
    time.sleep(random_delay(2, 0.5))
    
    page_num = args.start_page
    load_book_page(page_num)

    print('Scraping metadata...')
    time.sleep(random_delay(args.delay * 2, 0.4))
    
    failed = True
    for i in range(5):
        for request in driver.requests:
            if request.url == platform_identifiers['jigsaw_url'] + f'/books/{args.isbn}/pages':
                wait = 0
                while not request.response and wait < 30:
                    time.sleep(random_delay(1, 0.3))
                    wait += 1
                if not request.response or not request.response.body:
                    print('Failed to get pages information.')
                else:
                    book_info['pages'] = json.loads(request.response.body.decode())
            elif request.url == platform_identifiers['jigsaw_url'] + f'/info/books.json?isbns={args.isbn}':
                wait = 0
                while not request.response and wait < 30:
                    time.sleep(random_delay(1, 0.3))
                    wait += 1
                if not request.response or not request.response.body:
                    print('Failed to get book information.')
                else:
                    book_info['book'] = json.loads(request.response.body.decode())
            elif request.url == platform_identifiers['jigsaw_url'] + f'/books/{args.isbn}/toc':
                wait = 0
                while not request.response and wait < 30:
                    time.sleep(random_delay(1, 0.3))
                    wait += 1
                if not request.response or not request.response.body:
                    print('Failed to get TOC information, only got:', list(book_info.keys()))
                else:
                    book_info['toc'] = json.loads(request.response.body.decode())
        
        if 'pages' not in book_info.keys() or 'book' not in book_info.keys() or 'toc' not in book_info.keys():
            print('Missing some book data, only got:', list(book_info.keys()))
        else:
            failed = False
        
        if not failed:
            break
        
        retry_delay = random_delay(10, 0.5)
        print(f'Retrying metadata scrape in {retry_delay:.2f}s...')
        time.sleep(retry_delay)
        load_book_page(page_num)

    if args.only_scrape_metadata:
        driver.close()
        del driver

    if not args.only_scrape_metadata:
        _, total_pages = get_num_pages()

        if args.start_page > 0:
            print('You specified a start page so ignore the very large page count.')
        total_pages = 99999999999999999 if args.start_page > 0 else total_pages

        print('Total number of pages:', total_pages)
        print('Scraping pages...')

        page_urls = set()
        failed_pages = set()
        bar = tqdm(total=total_pages)
        bar.update(page_num)
        
        consecutive_failures = 0
        max_consecutive_failures = 5
        
        while page_num < total_pages + 1:
            # Random delay between pages with human-like variation
            delay = human_like_delay(args.min_delay, args.max_delay)
            time.sleep(delay)
            
            # Occasionally simulate human behavior
            if random.random() < 0.15:  # 15% chance
                simulate_human_behavior(driver)
            
            retry_delay = random_delay(5, 0.5)
            base_url = None
            
            for page_retry in range(3):
                for find_img_retry in range(3):
                    for request in driver.requests:
                        if request.url.startswith(platform_identifiers['jigsaw_url'] + f'/books/{args.isbn}/images/'):
                            base_url = request.url.split('/')
                            del base_url[-1]
                            base_url = '/'.join(base_url)
                    time.sleep(random_delay(1, 0.3))
                
                if base_url:
                    break
                
                bar.write(f'Could not find image for page {page_num}, sleeping {retry_delay:.2f}s...')
                time.sleep(retry_delay)
                retry_delay = random_delay(retry_delay + 3, 0.4)

            page, _ = get_num_pages()

            if not base_url:
                bar.write(f'Failed to get URL for page {page_num}, retrying later.')
                failed_pages.add(page_num)
                consecutive_failures += 1
                
                # If too many consecutive failures, take a longer break
                if consecutive_failures >= max_consecutive_failures:
                    long_break = random_delay(30, 0.5)
                    bar.write(f'Too many failures, taking a {long_break:.2f}s break...')
                    time.sleep(long_break)
                    consecutive_failures = 0
            else:
                page_urls.add((page, base_url))
                bar.write(base_url)
                consecutive_failures = 0
                
                try:
                    int(page)
                except ValueError:
                    total_pages += 1
                    non_number_pages += 1
                    bar.write(f'Non-number page {page}, increasing page count to: {total_pages}')
                    bar.total = total_pages
                    bar.refresh()

            if page_num == args.end_page:
                bar.write(f'Exiting on page {page_num}.')
                break

            if isinstance(page_num, int) and page_num > 0:
                try:
                    if driver.execute_script(
                        f'return document.querySelector("' + 
                        platform_identifiers['next_page_css'] + '").disabled'
                    ):
                        bar.write(f'Book completed, exiting.')
                        break
                except JavascriptException:
                    pass

            del driver.requests
            actions = ActionChains(driver)
            actions.send_keys(Keys.RIGHT)
            actions.perform()
            
            # Small random delay after key press
            time.sleep(random_delay(0.3, 0.5))
            
            bar.update()
            page_num += 1
        bar.close()

        print('Re-doing failed pages...')
        bar = tqdm(total=len(failed_pages))
        
        for page in failed_pages:
            load_book_page(page)
            
            delay = human_like_delay(args.min_delay, args.max_delay)
            time.sleep(delay)
            
            retry_delay = random_delay(5, 0.5)
            base_url = None
            
            for page_retry in range(3):
                for find_img_retry in range(3):
                    for request in driver.requests:
                        if request.url.startswith(platform_identifiers['jigsaw_url'] + f'/books/{args.isbn}/images/'):
                            base_url = request.url.split('/')
                            del base_url[-1]
                            base_url = '/'.join(base_url)
                    time.sleep(random_delay(1, 0.3))
                
                if base_url:
                    break
                
                bar.write(f'Could not find image for page {page_num}, sleeping {retry_delay:.2f}s...')
                time.sleep(retry_delay)
                retry_delay = random_delay(retry_delay + 3, 0.4)
            
            page, _ = get_num_pages()
            
            if not base_url:
                bar.write(f'Failed to get URL for page {page_num}')
            else:
                page_urls.add((page, base_url))
                bar.write(base_url)
            
            del driver.requests
            bar.update(1)
        bar.close()

        time.sleep(random_delay(2, 0.5))
        print('All pages scraped! Now downloading images...')
        print(f'DEBUG: Total page_urls to download: {len(page_urls)}')

        bar = tqdm(total=len(page_urls))
        download_failures = 0
        
        for page, base_url in page_urls:
            success = False
            
            for retry in range(6):
                del driver.requests
                
                # Random delay before download attempt
                delay = human_like_delay(args.min_delay, args.max_delay)
                time.sleep(delay)
                
                # Occasionally simulate human behavior during downloads
                if random.random() < 0.1:
                    simulate_human_behavior(driver)
                
                driver.get(f'{base_url.strip("/")}/2000')
                
                # Random wait time for response
                wait_time = random_delay(args.delay * 2, 0.4)
                time.sleep(wait_time)
                
                img_data = None
                
                # Wait for request with random intervals
                for wait_attempt in range(15):
                    for request in driver.requests:
                        if request.url.startswith(platform_identifiers['jigsaw_url'] + f'/books/{args.isbn}/images/'):
                            if request.response and request.response.body:
                                img_data = request.response.body
                                bar.write(f'DEBUG: Got image data for page {page}, size: {len(img_data)} bytes')
                                break
                    if img_data:
                        break
                    time.sleep(random_delay(1, 0.3))
                
                dl_file = ebook_files / f'{page}.jpg'
                
                if img_data:
                    try:
                        with open(dl_file, 'wb') as file:
                            file.write(img_data)
                        
                        if not dl_file.exists():
                            bar.write(f'ERROR: File {dl_file} was not created!')
                            continue
                            
                        img = Image.open(dl_file)
                        bar.write(f'DEBUG: Image dimensions for page {page}: {img.width}x{img.height}')
                        
                        if img.width < 1000:
                            bar.write(f'Image too small at {img.width}px wide, retrying: {base_url}')
                            img.close()
                            driver.get('https://google.com')
                            
                            # Random recovery delay
                            recovery_delay = random_delay(8, 0.5)
                            time.sleep(recovery_delay)
                            
                            load_book_page(0)
                            time.sleep(random_delay(8, 0.5))
                            continue
                        
                        img.save(dl_file, format='JPEG', subsampling=0, quality=100)
                        img.close()
                        success = True
                        bar.write(f'SUCCESS: Saved page {page} to {dl_file}')
                    except Exception as e:
                        bar.write(f'ERROR saving image for page {page}: {str(e)}')
                        if dl_file.exists():
                            dl_file.unlink()
                        continue
                else:
                    bar.write(f'No image data found for page {page} on attempt {retry+1}')
                    
                    # Increase delay on repeated failures
                    if retry > 2:
                        extra_delay = random_delay(5, 0.5)
                        bar.write(f'Taking extra break: {extra_delay:.2f}s')
                        time.sleep(extra_delay)
                
                if success:
                    download_failures = 0
                    break
                    
                # If multiple retries failing, take a longer break
                if retry >= 3:
                    long_break = random_delay(15, 0.5)
                    bar.write(f'Multiple failures, taking {long_break:.2f}s break...')
                    time.sleep(long_break)
            
            if not success:
                bar.write(f'FAILED to download image after all retries: {base_url}')
                download_failures += 1
                
                # If too many download failures, suggest a break
                if download_failures >= 5:
                    bar.write('WARNING: Multiple download failures. Consider taking a manual break.')
                    download_failures = 0
            
            bar.update()
        bar.close()
        
        downloaded_files = list(ebook_files.iterdir())
        print(f'\n=== DOWNLOAD SUMMARY ===')
        print(f'Total files downloaded: {len(downloaded_files)}')
        print(f'Files in output folder: {sorted([f.name for f in downloaded_files])}')
        
        driver.close()
        del driver
else:
    print('Page scrape skipped...')

print('Checking for blank pages...')
existing_page_files = move_romans_to_front(
    roman_sort_with_ints([try_convert_int(str(x.stem)) for x in list(ebook_files.iterdir())])
)
print(f'DEBUG: Found {len(existing_page_files)} existing page files')

if non_number_pages == 0:
    for item in existing_page_files:
        if isinstance(try_convert_int(item), str):
            non_number_pages += 1

for page in tqdm(iterable=existing_page_files):
    page_i = try_convert_int(page)
    if isinstance(page_i, int) and page_i > 0:
        page_i += non_number_pages
        last_page_i = try_convert_int(existing_page_files[page_i - 1])
        if isinstance(last_page_i, int):
            last_page_i = last_page_i + non_number_pages
            if last_page_i != page_i - 1:
                img = Image.new('RGB', (2000, 2588), (255, 255, 255))
                img.save(ebook_files / f'{int(page) - 1}.jpg')
                tqdm.write(f'Created blank image for page {int(page) - 1}.')

print('Building PDF...')
raw_pdf_file = args.output / f'{args.isbn} RAW.pdf'
existing_page_files = move_romans_to_front(
    roman_sort_with_ints([try_convert_int(str(x.stem)) for x in list(ebook_files.iterdir())])
)
page_files = [str(ebook_files / f'{x}.jpg') for x in existing_page_files]

if not page_files:
    print('ERROR: No images found to create PDF!')
    exit(1)

pdf = img2pdf.convert(page_files)
with open(raw_pdf_file, 'wb') as f:
    f.write(pdf)

if 'book' in book_info.keys() and 'books' in book_info['book'].keys() and len(book_info['book']['books']):
    title = book_info['book']['books'][0]['title']
    author = book_info['book']['books'][0]['author']
else:
    title = args.isbn
    author = 'Unknown'

if not args.skip_ocr:
    print('Running OCR...')
    ocr_in = raw_pdf_file
    _, raw_pdf_file_path = tempfile.mkstemp(suffix='.pdf')
    subprocess.run(
        f'ocrmypdf -l {args.language} --title "{title}" --jobs $(nproc) --output-type pdfa "{ocr_in}" "{raw_pdf_file_path}"',
        shell=True
    )
    raw_pdf_file = raw_pdf_file_path
else:
    print('Skipping OCR...')

print('Adding metadata...')
with open(raw_pdf_file, 'rb') as file_in:
    pdf_reader = PdfReader(file_in)
    pdf_writer = PdfWriter()
    
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)
    
    pdf_writer.add_metadata({'/Author': author, '/Title': title, '/Creator': f'ISBN: {args.isbn}'})

    if 'toc' in book_info.keys():
        print('Creating TOC...')
        for item in book_info['toc']:
            pdf_writer.add_outline_item(item['title'], int(item['cfi'].strip('/')) - 1)
    else:
        print('Not creating TOC...')

    _, tmpfile = tempfile.mkstemp(suffix='.pdf')
    with open(tmpfile, 'wb') as tmp_out:
        pdf_writer.write(tmp_out)

romans_end = 0
for p in existing_page_files:
    if isinstance(p, str):
        romans_end += 1

if romans_end > 0:
    print('Renumbering pages...')
    reader = PdfReader(tmpfile)
    labels = PageLabels.from_pdf(reader)

    roman_labels = PageLabelScheme(
        startpage=0,
        style='none',
        prefix='Cover',
        firstpagenum=1
    )
    labels.append(roman_labels)

    roman_labels = PageLabelScheme(
        startpage=1,
        style='roman lowercase',
        firstpagenum=1
    )
    labels.append(roman_labels)

    normal_labels = PageLabelScheme(
        startpage=romans_end,
        style='arabic',
        firstpagenum=1
    )
    labels.append(normal_labels)

    labels.write(reader)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    with open(args.output / f'{title}.pdf', 'wb') as output_file:
        writer.write(output_file)
else:
    shutil.move(tmpfile, args.output / f'{title}.pdf')

if os.path.exists(tmpfile):
    os.remove(tmpfile)

if args.compress:
    print('Compressing PDF...')
    reader = PdfReader(args.output / f'{title}.pdf')
    writer = PdfWriter()
    for page in reader.pages:
        page.compress_content_streams()
        writer.add_page(page)
    with open(args.output / f'{title} compressed.pdf', 'wb') as f:
        writer.write(f)

print(f'\n=== COMPLETED ===')
print(f'Final PDF: {args.output / f"{title}.pdf"}')