import os
import shutil
import pyautogui
import time
import subprocess
import sys
import psutil

# 리소스 경로 설정 함수
def resource_path(relative_path):
    try:
        # PyInstaller로 패키징된 경우 임시 경로 설정
        base_path = sys._MEIPASS
    except Exception:
        # 개발 환경에서 실행할 경우 현재 디렉토리 사용
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def find_image(file_path, confidence):
    window_detected = None
    while not window_detected:
        try:
            window_detected = pyautogui.locateOnScreen(file_path, confidence=confidence)
            time.sleep(1)
        except Exception as e:
            time.sleep(1)
    x, y, width, height = window_detected
    return x, y, width, height

def button_click(x, y):
    pyautogui.click(x,y)
    time.sleep(0.2)

# 시스템에 연결된 드라이브 목록 가져오기
def get_usb_drives():
    drives = []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        if 'removable' in partition.opts:  # USB 드라이브를 필터링
            drives.append(partition.device)
    return drives

# USB 드라이브 목록 출력 및 선택
usb_drives = get_usb_drives()

if not usb_drives:
    print("USB 드라이브가 연결되지 않았습니다.")
    sys.exit()
else:
    print("다음 USB 드라이브가 연결되어 있습니다:")
    for idx, drive in enumerate(usb_drives):
        print(f"{idx + 1}. {drive}")

    # 사용자에게 드라이브 선택 요청
    selected_drive_index = int(input("사용할 USB 드라이브 번호를 입력하세요: ")) - 1
    selected_drive = usb_drives[selected_drive_index]

    if os.path.exists(selected_drive) and os.path.isdir(selected_drive):
        print(f"선택된 USB 드라이브: {selected_drive}")
    else:
        print("선택한 드라이브가 유효하지 않습니다.")
        sys.exit()

select_drive = selected_drive[0]

# 바탕화면 경로 설정
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# 복사할 파일 목록
files_to_copy = [
    f"{select_drive}:/1. 지엔텔/0. ※ 기본 프로그램 설치 방법 및 설치파일/1.OfficeCoreTalkSetup.zip",
    f"{select_drive}:/1. 지엔텔/0. ※ 기본 프로그램 설치 방법 및 설치파일/2.Duzon ERP iU Browser Setup.zip",
    f"{select_drive}:/1. 지엔텔/0. ※ 기본 프로그램 설치 방법 및 설치파일/4.tgsvpn_setup_x64.zip",
    f"{select_drive}:/1. 지엔텔/0. ※ 기본 프로그램 설치 방법 및 설치파일/BANDIZIP-SETUP-STD-X64.EXE",
    f"{select_drive}:/1. 지엔텔/2. MS Office/VC_redist.x64.exe",
    f"{select_drive}:/1. 지엔텔/2. MS Office/vc_redist.x86.exe",
    f"{select_drive}:/1. 지엔텔/2. MS Office/MS Office2019-kor/Microsoft_Office_2019_Professional_Plus_x64.iso",
    f"{select_drive}:/1. 지엔텔/3. V3/AhnLab V3 Internet Security 9.0 (2).exe",
    #f"{select_drive}:/1. 지엔텔/3. V3/V3 Serial_PC.txt",
    f"{select_drive}:/1. 지엔텔/4-1. Sweeper/[SWeeper]지엔텔_배포에이전트/SWeeper_Agent_(220.95.197.12)_showuser.exe"
]

confidence = 0.8

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
subprocess.run(['powershell', 'Expand-Archive', '-LiteralPath', f'"{desktop_path}/2.Duzon ERP iU Browser Setup.zip"', '-DestinationPath', f'"{desktop_path}/Duzon ERP iU Browser Setup"', '-Force'])
subprocess.run(['powershell', 'Expand-Archive', '-LiteralPath', f'{desktop_path}/4.tgsvpn_setup_x64.zip', '-DestinationPath', f'{desktop_path}/tgsvpn_setup_x64', '-Force'])

# pyautogui 사용해 설치 과정 자동화
print("설치 과정 자동화 시작...")


Bandizip_path = "C:/Program Files/Bandizip"
if os.path.exists(Bandizip_path) and os.path.isdir(Bandizip_path):
    print("Bandizip이 존재합니다.")
else:
    # 1. Bandizip 설치
    print("Bandizip 설치 중 . . .")
    
    subprocess.run([os.path.join(desktop_path, "BANDIZIP-SETUP-STD-X64.EXE"), "/S"])
    
    

# 2. OfficeCoreTalk 설치
OfficeCoreTalk_path = "C:/Program Files (x86)/OfifceCoreTalk"
if os.path.exists(OfficeCoreTalk_path) and os.path.isdir(OfficeCoreTalk_path):
    print("OfficeCoreTalk가 존재합니다.")
else:
    print("OfficeCoreTalk 설치 중 . . .")
    proc = subprocess.Popen([os.path.join(desktop_path, "OfficeCoreTalkSetup", "OfficeCoreTalkSetup.exe"), "/S"])
    
    x, y, width, height = find_image(resource_path('talk1.png'), confidence)
    
    #버튼 위치
    button_x = x + width - 150
    button_y = y + height - 20
    
    click_x = x + width - 400
    click_y = y + height - 95
    
    button_click(button_x,button_y)
    button_click(click_x, click_y)
    button_click(button_x,button_y)
    button_click(button_x,button_y)
    button_click(button_x,button_y)
    
    x, y, width, height = find_image(resource_path('talk2.png'), confidence)
    
    check_x = x + width - 290
    check_y = y + height - 200
    
    button_click(check_x, check_y)
    button_click(button_x,button_y)

ERP_path = "C:/ERPU/Browser"
if os.path.exists(ERP_path) and os.path.isdir(ERP_path):
    print("ERP가 존재합니다.")
else:
    # 3. Duzon ERP 설치
    print("Duzon ERP iU Browser Setup 설치 중 . . .")
    subprocess.Popen([os.path.join(desktop_path, "Duzon ERP iU Browser Setup", "Duzon ERP iU Browser Setup.exe")])
    #subprocess.Popen([f'"{desktop_path}/Duzon ERP iU Browser Setup/Duzon ERP iU Browser Setup.exe"'])
    
    x, y, width, height = find_image(resource_path('erp1.png'), confidence)
    
    button_x = x + width - 330
    button_y = y + height - 20
    
    button_click(button_x, button_y)
    
    click_x = x + width - 350
    click_y = y + height - 100
    button_click(click_x, click_y)
    button_click(button_x, button_y)
    time.sleep(1)
    x, y, width, height = find_image(resource_path('erp2.png'), 0.9)
    button_click(button_x, button_y)
    x, y, width, height = find_image(resource_path('erp3.png'), confidence)
    input_x_1 = x + width - 350
    input_y_1 = y + height - 430
    button_click(input_x_1, input_y_1)
    pyautogui.write("http://220.95.197.11/ERP-U")
    button_click(input_x_1, input_y_1 + 62)
    pyautogui.write("http://220.95.197.11/ERP-U")
    button_click(input_x_1, input_y_1 + 62 + 62)
    pyautogui.write("GNTU")
    check_button_x = x + width - 350
    check_button_y = y + height - 100
    button_click(check_button_x,check_button_y)
    x, y, width, height = find_image(resource_path('erp4.png'), confidence)
    erp_close_x_1 = x + width - 20
    erp_close_y_1 = y + 20
    button_click(erp_close_x_1,erp_close_y_1)
    erp_close_x_2 = x + (width/2) - 30
    erp_close_y_2 = y + (height/2) + 70
    button_click(erp_close_x_2,erp_close_y_2)

VPN_path = "C:/Program Files/AhnLab/VPN"
if os.path.exists(VPN_path) and os.path.isdir(VPN_path):
    print("VPN가 존재합니다.")
else:
    # 4. tgsvpn 설치
    print("tgsvpn 설치 중 . . .")
    
    subprocess.Popen([os.path.join(desktop_path, "tgsvpn_setup_x64", "tgsvpn_setup_x64.exe")])
    x, y, width, height = find_image(resource_path('vpn1.png'), confidence)
    vpn_button_x_1 = x + width - 110
    vpn_button_y_1 = y + height - 30
    button_click(vpn_button_x_1,vpn_button_y_1)
    x, y, width, height = find_image(resource_path('vpn2.png'), confidence)
    vpn_button_x_2 = x + width - 150
    vpn_button_y_2 = y + height - 30
    button_click(vpn_button_x_2,vpn_button_y_2)
    vpn_button_x_3 = x + 50
    vpn_button_y_3 = y + height - 60
    button_click(vpn_button_x_3,vpn_button_y_3)
    button_click(vpn_button_x_2,vpn_button_y_2)
    x, y, width, height = find_image(resource_path('vpn3.png'), confidence)
    vpn_button_x_4 = x + 30
    vpn_button_y_4 = y + (height/2)
    button_click(vpn_button_x_4,vpn_button_y_4)
    vpn_button_x_5 = x + width - 50
    vpn_button_y_5 = y + height - 30
    button_click(vpn_button_x_5,vpn_button_y_5)

# 5. VC_redist.x64 설치
print("VC_redist.x64 설치 중 . . .")
subprocess.run([os.path.join(desktop_path, "VC_redist.x64.exe"), "/quiet", "/norestart"])



Microsoft_path = "C:/Program Files/Microsoft Office/root/Office16"
if os.path.exists(Microsoft_path) and os.path.isdir(Microsoft_path):
    print("Microsoft Office가 존재합니다.")
else:
    # ISO 파일 마운트
    print("ISO 파일 마운트 중 . . .")
    
    iso_path = os.path.join(desktop_path, "Microsoft_Office_2019_Professional_Plus_x64.iso")
    subprocess.run(['powershell', 'Mount-DiskImage', '-ImagePath', iso_path])
    
    # 마운트된 가상 드라이브 문자 찾기
    try:
        # 드라이브 문자 찾기 (Get-DiskImage로 DevicePath 찾고, Get-Volume으로 드라이브 문자 확인)
        drive_letter = subprocess.check_output([
            'powershell', '-command',
            f"(Get-Volume -DiskImage (Get-DiskImage -ImagePath '{iso_path}')).DriveLetter"
        ]).decode().strip()
    
        if drive_letter:
            print(f"마운트된 가상 드라이브 문자: {drive_letter}:\\")
        else:
            print("드라이브 문자를 찾을 수 없습니다.")
    except subprocess.CalledProcessError as e:
        print(f"드라이브 문자를 찾는 데 실패했습니다: {e}")

    # setup.bat 실행
    subprocess.run([f"{drive_letter}:/setup.bat"])

    x, y, width, height = find_image(resource_path('ms1.png'), confidence)
    ms_button_x_1 = x + (width/2)
    ms_button_y_1 = y + height - 20
    button_click(ms_button_x_1, ms_button_y_1)
    start_path = os.path.join("C:", "Program Files", "Microsoft Office", "root", "Office16", "EXCEL.EXE")
    os.startfile(start_path)
    x, y, width, height = find_image(resource_path('ms2.png'), confidence)
    ms_button_x_2 = x + width - 20
    ms_button_y_2 = y + height - 20
    button_click(ms_button_x_2, ms_button_y_2)
    x, y, width, height = find_image(resource_path('ms3.png'), confidence)
    ms_button_x_3 = x + width - 20
    ms_button_y_3 = y + height - 150
    button_click(ms_button_x_3, ms_button_y_3)
    x, y, width, height = find_image(resource_path('ms4.png'), confidence)
    time.sleep(3)
    ms_button_x_4 = x + 20
    ms_button_y_4 = y + height - 55
    button_click(ms_button_x_4, ms_button_y_4)
    x, y, width, height = find_image(resource_path('ms5.png'), confidence)
    ms_button_x_5 = x + (width/2)
    ms_button_y_5 = y + (height/2) + 73
    button_click(ms_button_x_5, ms_button_y_5)
    pyautogui.write("378NY-6WB8T-BVDWB-CPF28-W46T3")
    x, y, width, height = find_image(resource_path('ms6.png'), 0.9)
    ms_button_x_6 = x + (width/2)
    ms_button_y_6 = y + (height/2)
    button_click(ms_button_x_6, ms_button_y_6)
    x, y, width, height = find_image(resource_path('ms7.png'), 0.9)
    ms_button_x_7 = x + (width/2)
    ms_button_y_7 = y + (height/2)
    button_click(ms_button_x_7, ms_button_y_7)
    x, y, width, height = find_image(resource_path('ms8.png'), 0.9)
    ms_button_x_8 = x + width - 15
    ms_button_y_8 = y + 15
    button_click(ms_button_x_8, ms_button_y_8)
    # ISO 파일 마운트 해제
    time.sleep(1)
    print("ISO 파일 마운트 해제 중 . . .")
    subprocess.run(['powershell', 'Dismount-DiskImage', '-ImagePath', f'{desktop_path}/Microsoft_Office_2019_Professional_Plus_x64.iso'])


V3_path = "C:/Program Files/AhnLab/V3IS90"
if os.path.exists(V3_path) and os.path.isdir(V3_path):
    print("V3가 존재합니다.")
else:
    # 7. AhnLab V3 설치
    print("AhnLab V3 설치 중 . . .")
    
    subprocess.run([os.path.join(desktop_path, "AhnLab V3 Internet Security 9.0 (2).exe"), "/S"])




SWeeper_path = "C:/Program Files/SWeeper-N/Agent"
if os.path.exists(SWeeper_path) and os.path.isdir(SWeeper_path):
    print("SWeeper가 존재합니다.")
else:
    # 8. SWeeper 설치
    print("SWeeper 설치 중 . . .")
    
    subprocess.run([os.path.join(desktop_path, "SWeeper_Agent_(220.95.197.12)_showuser.exe"), "/S"])


print("모든 작업이 완료되었습니다.")