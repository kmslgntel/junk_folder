@echo off
rem UTF-8 코드 페이지 설정
chcp 65001 >nul
echo 바탕화면에서 파일과 폴더를 삭제하는 중입니다...

:: 복사된 파일 삭제
del /q "%USERPROFILE%\Desktop\1.OfficeCoreTalkSetup.zip"
del /q "%USERPROFILE%\Desktop\2.Duzon ERP iU Browser Setup.zip"
del /q "%USERPROFILE%\Desktop\4.tgsvpn_setup_x64.zip"
del /q "%USERPROFILE%\Desktop\BANDIZIP-SETUP-STD-X64.EXE"
del /q "%USERPROFILE%\Desktop\VC_redist.x64.exe"
del /q "%USERPROFILE%\Desktop\vc_redist.x86.exe"
del /q "%USERPROFILE%\Desktop\Microsoft_Office_2019_Professional_Plus_x64.iso"
del /q "%USERPROFILE%\Desktop\AhnLab V3 Internet Security 9.0 (2).exe"
del /q "%USERPROFILE%\Desktop\V3 Serial_PC.txt"
del /q "%USERPROFILE%\Desktop\SWeeper_Agent_(220.95.197.12)_showuser.exe"

:: 압축 해제된 폴더 삭제
rd /s /q "%USERPROFILE%\Desktop\OfficeCoreTalkSetup"
rd /s /q "%USERPROFILE%\Desktop\Duzon ERP iU Browser Setup"
rd /s /q "%USERPROFILE%\Desktop\tgsvpn_setup_x64"

echo 모든 파일과 폴더가 삭제되었습니다.
pause
