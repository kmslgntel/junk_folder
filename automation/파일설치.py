import os
import shutil
import pyautogui
import time
import subprocess

# 사용자로부터 드라이브 입력 받기
usb_drive = input("복사할 파일이 있는 USB 드라이브 문자를 입력하세요 (예: F): ")

# 바탕화면 경로 설정
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# 복사할 파일 목록
files_to_copy = [
    f"{usb_drive}:/1. 지엔텔/0. ※ 기본 프로그램 설치 방법 및 설치파일/1.OfficeCoreTalkSetup.zip",
    f"{usb_drive}:/1. 지엔텔/0. ※ 기본 프로그램 설치 방법 및 설치파일/2.Duzon ERP iU Browser Setup.zip",
    f"{usb_drive}:/1. 지엔텔/0. ※ 기본 프로그램 설치 방법 및 설치파일/4.tgsvpn_setup_x64.zip",
    f"{usb_drive}:/1. 지엔텔/0. ※ 기본 프로그램 설치 방법 및 설치파일/BANDIZIP-SETUP-STD-X64.EXE",
    f"{usb_drive}:/1. 지엔텔/2. MS Office/VC_redist.x64.exe",
    f"{usb_drive}:/1. 지엔텔/2. MS Office/vc_redist.x86.exe",
    f"{usb_drive}:/1. 지엔텔/2. MS Office/MS Office2019-kor/Microsoft_Office_2019_Professional_Plus_x64.iso",
    f"{usb_drive}:/1. 지엔텔/3. V3/AhnLab V3 Internet Security 9.0 (2).exe",
    f"{usb_drive}:/1. 지엔텔/3. V3/V3 Serial_PC.txt",
    f"{usb_drive}:/1. 지엔텔/4-1. Sweeper/[SWeeper]지엔텔_배포에이전트/SWeeper_Agent_(220.95.197.12)_showuser.exe"
]

# 파일 복사
print("파일을 바탕화면으로 복사 중 . . .")
for file in files_to_copy:
    if os.path.exists(file):
        shutil.copy(file, desktop_path)
        print(f"{file} 복사 완료.")
    else:
        print(f"파일 {file}을 찾을 수 없습니다.")

# 압축 해제
print("ZIP 파일 압축 해제 중 . . .")
subprocess.run(['powershell', 'Expand-Archive', '-LiteralPath', f'{desktop_path}/1.OfficeCoreTalkSetup.zip', '-DestinationPath', f'{desktop_path}/OfficeCoreTalkSetup', '-Force'])
subprocess.run(['powershell', 'Expand-Archive', '-LiteralPath', f'{desktop_path}/2.Duzon ERP iU Browser Setup.zip', '-DestinationPath', f'{desktop_path}/Duzon ERP iU Browser Setup', '-Force'])
subprocess.run(['powershell', 'Expand-Archive', '-LiteralPath', f'{desktop_path}/4.tgsvpn_setup_x64.zip', '-DestinationPath', f'{desktop_path}/tgsvpn_setup_x64', '-Force'])

# pyautogui 사용해 설치 과정 자동화
print("설치 과정 자동화 시작...")

# 1. Bandizip 설치
print("Bandizip 설치 중 . . .")
subprocess.run([f"{desktop_path}/BANDIZIP-SETUP-STD-X64.EXE", "/S"])

# 2. OfficeCoreTalk 설치
print("OfficeCoreTalk 설치 중 . . .")
subprocess.run([f"{desktop_path}/OfficeCoreTalkSetup/OfficeCoreTalkSetup.exe", "/S"])

# 3. Duzon ERP 설치
print("Duzon ERP iU Browser Setup 설치 중 . . .")
subprocess.run([f"{desktop_path}/Duzon ERP iU Browser Setup/Duzon ERP iU Browser Setup.exe", "/S"])

# 설치 프로그램 창이 나타날 때까지 대기 (예: '다음' 버튼이나 설치 프로그램 제목 바 이미지로 확인)
window_detected = None
while not window_detected:
    window_detected = pyautogui.locateOnScreen('ERP_IU_setup_image.png')  # 설치 프로그램 창이나 버튼 이미지
    time.sleep(1)  # 1초 간격으로 창이 떴는지 반복 확인





# 비즈니스 호스트 서버 URL 설정
print("Business Host Server URL : http://220.95.197.11/ERP-U")
print("Assembly Host Server URL : http://220.95.197.11/ERP-U")
print("Server Key : GNTU")

# 4. tgsvpn 설치
print("tgsvpn 설치 중 . . .")
subprocess.run([f"{desktop_path}/tgsvpn_setup_x64/tgsvpn_setup_x64.exe", "/S"])

# 5. VC_redist.x64 설치
print("VC_redist.x64 설치 중 . . .")
subprocess.run([f"{desktop_path}/VC_redist.x64.exe", "/quiet", "/norestart"])

# 6. ISO 파일 마운트 및 설치
print("ISO 파일 마운트 중 . . .")
subprocess.run(['powershell', 'Mount-DiskImage', '-ImagePath', f'{desktop_path}/Microsoft_Office_2019_Professional_Plus_x64.iso'])

# 마운트된 가상 드라이브 문자 찾기 및 이동
drive_letter = subprocess.check_output(['powershell', '-command', '(Get-DiskImage -ImagePath "' + f'{desktop_path}/Microsoft_Office_2019_Professional_Plus_x64.iso").DevicePath']).decode().strip()

# setup.bat 실행
subprocess.run([f"{drive_letter}:/setup.bat"])

# 제품 키 출력
print("제품 키: 378NY-6WB8T-BVDWB-CPF28-W46T3")

# 7. AhnLab V3 설치
print("AhnLab V3 설치 중 . . .")
subprocess.run([f"{desktop_path}/AhnLab V3 Internet Security 9.0 (2).exe", "/S"])

# V3 제품 키 출력
print("V3 제품 키: 97043410-01165701")

# 8. SWeeper 설치
print("SWeeper 설치 중 . . .")
subprocess.run([f"{desktop_path}/SWeeper_Agent_(220.95.197.12)_showuser.exe", "/S"])

# ISO 파일 마운트 해제
print("ISO 파일 마운트 해제 중 . . .")
subprocess.run(['powershell', 'Dismount-DiskImage', '-ImagePath', f'{desktop_path}/Microsoft_Office_2019_Professional_Plus_x64.iso'])

print("모든 작업이 완료되었습니다.")
