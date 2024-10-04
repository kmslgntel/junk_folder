@echo off
rem UTF-8 코드 페이지 설정
chcp 65001 >nul

rem 네트워크 유형 선택
set /p network_type="네트워크 유형을 선택하세요 (1: 유선, 2: 무선): "

if "%network_type%"=="1" (
    set adapter_name="이더넷"
) else if "%network_type%"=="2" (
    set adapter_name="Wi-Fi"
) else (
    echo 잘못된 입력입니다. 배치 파일을 종료합니다.
    exit /b
)

:input_ip
rem IP 주소 입력
set /p ip_address="사용할 IP 주소를 입력하세요 (예: 192.168.1.50): "

rem A 클래스와 B 클래스가 192.168인지 확인
echo %ip_address% | findstr /r "^192\.168\." >nul
if errorlevel 1 (
    echo IP 주소는 반드시 192.168.x.x 형식이어야 합니다. 다시 입력해주세요.
    goto input_ip
)

rem C 클래스 값이 1, 2, 4, 5 중 하나인지 확인
for /f "tokens=3 delims=." %%a in ("%ip_address%") do (
    if "%%a"=="1" goto check_d_class
    if "%%a"=="2" goto check_d_class
    if "%%a"=="4" goto check_d_class
    if "%%a"=="5" goto check_d_class
)

echo 잘못된 C 클래스 값입니다. 다시 입력해주세요.
goto input_ip

:check_d_class
rem D 클래스 값이 2부터 255 사이인지 확인
for /f "tokens=4 delims=." %%b in ("%ip_address%") do (
    if %%b geq 2 if %%b leq 254 goto valid_ip
)

echo D 클래스 값은 2부터 254 사이의 숫자여야 합니다. 다시 입력해주세요.
goto input_ip

:valid_ip
rem 서브넷 마스크 설정
set subnet_mask=255.255.255.0

rem 게이트웨이 자동 설정
for /f "tokens=1-3 delims=." %%a in ("%ip_address%") do (
    set gateway=%%a.%%b.%%c.1
)

rem 네트워크 설정 적용
netsh interface ip set address name=%adapter_name% static %ip_address% %subnet_mask% %gateway%
netsh interface ip set dns name=%adapter_name% static 218.159.102.251

rem 설정 확인
ipconfig /all

echo IP 설정이 완료되었습니다.
pause
