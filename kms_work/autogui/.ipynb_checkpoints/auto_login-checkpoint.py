import pyautogui
import json
import time
from cryptography.fernet import Fernet
import os
import subprocess
import pyperclip

# JSON 파일 경로와 암호화된 자격 증명 파일 경로
json_file_path = "coordinates.json"
credentials_file_path = "credentials.enc"
key_path = "secret.key"

def get_current_directory():
    return os.path.dirname(os.path.abspath(__file__))

current_path = get_current_directory()

# 암호화 키 로드
if os.path.exists(key_path):
    with open(key_path, 'rb') as key_file:
        key = key_file.read()
else:
    raise FileNotFoundError("암호화 키 파일을 찾을 수 없습니다.")

cipher_suite = Fernet(key)

# 좌표 데이터 로드
if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as file:
        coordinates = json.load(file)
else:
    raise FileNotFoundError("좌표 JSON 파일을 찾을 수 없습니다.")

# 암호화된 자격 증명 로드
if os.path.exists(credentials_file_path):
    with open(credentials_file_path, 'rb') as enc_file:
        encrypted_id, encrypted_pw = enc_file.read().split(b'\n')
        id_data = cipher_suite.decrypt(encrypted_id).decode()
        pw_data = cipher_suite.decrypt(encrypted_pw).decode()
else:
    raise FileNotFoundError("자격 증명 파일을 찾을 수 없습니다.")

# 마우스 클릭 함수
def click_at(coordinate):
    pyautogui.click(coordinate['x'], coordinate['y'])

# ID와 PW 입력 함수
def type_credentials(id_data, pw_data):
    #pyautogui.typewrite(id_data)
    pyperclip.copy(id_data)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)
    pyautogui.press('tab')
    #pyautogui.typewrite(pw_data)
    time.sleep(0.1)
    pyperclip.copy(pw_data)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)
    pyautogui.press('enter')


# 스토브 클라이언트 실행
#subprocess.Popen("C:\\Program Files (x86)\\STOVE\\STOVE.exe")
#time.sleep(10)  # 클라이언트가 완전히 실행될 때까지 대기


# 자동화 시작
time.sleep(2)  # 시작 전에 2초 대기 (필요에 따라 조정)
# 이미지 기반 로그 버튼 클릭
logo_image_path = os.path.join(current_path, "image", "logo.png")
logo_button_location = None
while logo_button_location is None:
    try:
        logo_button_location = pyautogui.locateOnScreen(logo_image_path, confidence=0.8)
        if logo_button_location:
            pyautogui.click(logo_button_location)
            print("Logo button clicked")
        else:
            print("Logo button not found, retrying in 2 seconds...")
            time.sleep(2)
    except pyautogui.ImageNotFoundException:
        print("Logo button image not found, retrying in 2 seconds...")
        time.sleep(2)
time.sleep(1)

# 이미지 기반 ID 버튼 클릭
ID_image_path = os.path.join(current_path, "image", "ID.png")
ID_button_location = None
while ID_button_location is None:
    try:
        ID_button_location = pyautogui.locateOnScreen(ID_image_path, confidence=0.8)
        if ID_button_location:
            pyautogui.click(ID_button_location)
            print("ID button clicked")
        else:
            print("ID button not found, retrying in 2 seconds...")
            time.sleep(2)
    except pyautogui.ImageNotFoundException:
        print("ID button image not found, retrying in 2 seconds...")
        time.sleep(2)
time.sleep(1)


type_credentials(id_data, pw_data)

# 로그인 완료를 기다리는 시간 (필요에 따라 조정)
time.sleep(5)

# 이미지 기반 탭 버튼 클릭
gametab_image_path = os.path.join(current_path, "image", "gametab.png")
logo_button_location = None
while logo_button_location is None:
    try:
        logo_button_location = pyautogui.locateOnScreen(gametab_image_path, confidence=0.8)
        if logo_button_location:
            pyautogui.click(logo_button_location)
            print("Gametab button clicked")
        else:
            print("Gametab button not found, retrying in 2 seconds...")
            time.sleep(2)
    except pyautogui.ImageNotFoundException:
        print("Gametab button image not found, retrying in 2 seconds...")
        time.sleep(2)
time.sleep(1)

# 이미지 기반 시작 버튼 클릭
start_image_path = os.path.join(current_path, "image", "start.png")
start_button_location = None
while start_button_location is None:
    try:
        start_button_location = pyautogui.locateOnScreen(start_image_path, confidence=0.8)
        if start_button_location:
            pyautogui.click(start_button_location)
            print("Start button clicked")
        else:
            print("Start button not found, retrying in 2 seconds...")
            time.sleep(2)
    except pyautogui.ImageNotFoundException:
        print("Start button image not found, retrying in 2 seconds...")
        time.sleep(2)
time.sleep(1)
