@echo off
rem UTF-8 코드 페이지 설정
chcp 65001 >nul
echo 모든 네트워크 어댑터의 IP 및 DNS 설정을 DHCP로 변경 중...

:: 모든 네트워크 어댑터의 IP 주소를 DHCP로 변경
for /f "tokens=*" %%a in ('netsh interface show interface ^| findstr /C:"Connected"') do (
    set "adapter_name=%%a"
    set "adapter_name=!adapter_name:~23!"
    echo IP 설정을 DHCP로 변경 중: !adapter_name!
    netsh interface ip set address name="!adapter_name!" source=dhcp
)

:: 모든 네트워크 어댑터의 DNS 설정을 DHCP로 변경
for /f "tokens=*" %%a in ('netsh interface show interface ^| findstr /C:"Connected"') do (
    set "adapter_name=%%a"
    set "adapter_name=!adapter_name:~23!"
    echo DNS 설정을 DHCP로 변경 중: !adapter_name!
    netsh interface ip set dns name="!adapter_name!" source=dhcp
)

echo 모든 네트워크 어댑터의 DHCP 설정이 완료되었습니다.
pause
