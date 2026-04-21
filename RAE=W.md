

C:\Windows\System32>dir C:\npiperelay\
 Volume in drive C is Local Disk
 Volume Serial Number is A2DC-3982

 Directory of C:\npiperelay

04/21/2026  03:55 PM    <DIR>          .                                                                                                                                                                           07/02/2020  08:40 PM             1,068 LICENSE                                                                                                                                                                     07/02/2020  08:40 PM         1,872,384 npiperelay.exe                                                                                                                                                              07/02/2020  08:40 PM             8,086 README.md                                                                                                                                                                                  3 File(s)      1,881,538 bytes                                                                                                                                                                                     1 Dir(s)  62,128,660,480 bytes free                                                                                                                                                                                                                                                                                                                                                                                    C:\Windows\System32>where iproxy                                                                                                                                                                                   INFO: Could not find files for the given pattern(s).                                                                                                                                                                                                                                                                                                                                                                                  C:\Windows\System32>dir "C:\Program Files\Common Files\Apple\Apple Application Support\" 2>nul                                                                                                                      Volume in drive C is Local Disk                                                                                                                                                                                    Volume Serial Number is A2DC-3982                                                                                                                                                                                                                                                                                                                                                                                                     Directory of C:\Program Files\Common Files\Apple\Apple Application Support                                                                                                                                                                                                                                                                                                                                                           04/05/2026  05:07 AM    <DIR>          .                                                                                                                                                                           04/05/2026  05:17 AM    <DIR>          ..
07/24/2010  10:40 PM           628,224 iPHUCWIN32.exe
07/24/2010  10:40 PM           229,888 readline5.dll
               2 File(s)        858,112 bytes
               2 Dir(s)  62,128,660,480 bytes free                                                                                                                                                                                                                                                                                                                                                                                    C:\Windows\System32>dir "C:\Program Files\iTunes\" 2>nul                                                                                                                                                                                                                                                                                                                                                                              C:\Windows\System32>dir "C:\Program Files (x86)\iTunes\" 2>nul                                                                                                                                                                                                                                                                                                                                                                        C:\Windows\System32>powershell -command "Get-Process -Id (Get-NetTCPConnection -LocalPort 27015).OwningProcess | Select-Object Name, Id"

Name                       Id
----                       --
AppleMobileDeviceService 8048



C:\Windows\System32>
C:\Windows\System32>
C:\Windows\System32>
C:\Windows\System32>
C:\Windows\System32>
C:\Windows\System32>
C:\Windows\System32>powershell -command "Get-ChildItem \\.\pipe\ | Where-Object {$_.Name -like '*Apple*' -or $_.Name -like '*AMD*' -or $_.Name -like '*Lockdown*' -or $_.Name -like '*iphone*' -or $_.Name -like '*device*'}"

C:\Windows\System32>powershell -command "Test-NetConnection -ComputerName 127.0.0.1 -Port 27015"


ComputerName     : 127.0.0.1
RemoteAddress    : 127.0.0.1
RemotePort       : 27015
InterfaceAlias   : Loopback Pseudo-Interface 1
SourceAddress    : 127.0.0.1
TcpTestSucceeded : True




C:\Windows\System32>powershell -command "Test-NetConnection -ComputerName 127.0.0.1 -Port 27015"

C:\Windows\System32>powershell -command "(New-Object System.Net.Sockets.TcpClient('127.0.0.1', 27015)).Connected"
True

C:\Windows\System32>
