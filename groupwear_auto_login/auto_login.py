import subprocess
from encrypt_decrypt import decrypt_message
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import time
import os
import pyautogui

def get_current_directory():
    return os.path.dirname(os.path.abspath(__file__))

current_path = get_current_directory()
credentials_path = os.path.join(current_path, "credentials.enc")

# 암호화된 사용자 정보 로드 및 복호화
with open(credentials_path, "rb") as file:
    encrypted_username = file.readline().strip()
    encrypted_password = file.readline().strip()

username = decrypt_message(encrypted_username)
password = decrypt_message(encrypted_password)

# Chrome 디버깅 모드에서 실행
debugging_port = "9222"

# subprocess.Popen([chrome_path, f"--remote-debugging-port={debugging_port}", f"--user-data-dir={user_data_dir}"], shell=True)

# 잠시 대기 (Chrome이 완전히 시작될 시간을 줍니다)
#time.sleep(30)

# Chrome 디버깅 옵션 설정
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{debugging_port}")

# 웹드라이버 설정 및 기존 Chrome 창 연결
driver = None
while driver is None:
    try:
        driver = webdriver.Chrome(service=Service(), options=chrome_options)
        print("Driver connected successfully.")
        time.sleep(5)
    except WebDriverException as e:
        print(f"Driver connection failed: {e}")
        print("Retrying in 5 seconds...")
        time.sleep(5)  # 5초 간격으로 재시도

try:
    # 로그인 페이지로 이동
    driver.get("https://gw.lgntel.com/Account/Login2")  # 여기에 로그인 페이지 URL을 입력하세요
    print("URL Access...")
    time.sleep(2)

    # driver.set_window_position(0, 0)
    # driver.set_window_size(1024, 768)
    # pyautogui.click(512, 384)  # 창의 가운데 부분을 클릭
    # time.sleep(2)

    # 아이콘 기반 클릭
    icon_image_path = os.path.join(current_path, "image", "icon.png")
    icon_field_location = None
    while icon_field_location is None:
        try:
            icon_field_location = pyautogui.locateOnScreen(icon_image_path, confidence=0.8)
            if icon_field_location:
                pyautogui.click(icon_field_location)
                print("Icon field clicked")
            else:
                print("Icon field not found, retrying in 2 seconds...")
                time.sleep(2)
        except pyautogui.ImageNotFoundException:
            print("Icon field image not found, retrying in 2 seconds...")
            time.sleep(2)
    time.sleep(1)



    # 이미지 기반 ID 필드 클릭
    id_image_path = os.path.join(current_path, "image", "ID.png")
    id_field_location = None
    while id_field_location is None:
        try:
            id_field_location = pyautogui.locateOnScreen(id_image_path, confidence=0.8)
            if id_field_location:
                pyautogui.click(id_field_location)
                print("ID field clicked")
            else:
                print("ID field not found, retrying in 2 seconds...")
                time.sleep(2)
        except pyautogui.ImageNotFoundException:
            print("ID field image not found, retrying in 2 seconds...")
            time.sleep(2)
    time.sleep(1)

    # 사용자 이름 입력
    pyautogui.write(username)
    print("Input ID")
    time.sleep(1)

    # # 이미지 기반 비밀번호 필드 클릭
    # pw_image_path = os.path.join(current_path, "image", "PW.png")
    # pw_field_location = None
    # while pw_field_location is None:
    #     try:
    #         pw_field_location = pyautogui.locateOnScreen(pw_image_path, confidence=0.8)
    #         if pw_field_location:
    #             pyautogui.click(pw_field_location)
    #             print("Password field clicked")
    #         else:
    #             print("Password field not found, retrying in 2 seconds...")
    #             time.sleep(2)
    #     except pyautogui.ImageNotFoundException:
    #         print("Password field image not found, retrying in 2 seconds...")
    #         time.sleep(2)
    # time.sleep(0.1)

    pyautogui.press('tab')
    time.sleep(0.1)
    # 비밀번호 입력
    pyautogui.write(password)
    print("Input PW")
    time.sleep(0.1)

    # 이미지 기반 로그인 버튼 클릭
    login_image_path = os.path.join(current_path, "image", "Login.png")
    login_button_location = None
    while login_button_location is None:
        try:
            login_button_location = pyautogui.locateOnScreen(login_image_path, confidence=0.8)
            if login_button_location:
                pyautogui.click(login_button_location)
                print("Login button clicked")
            else:
                print("Login button not found, retrying in 2 seconds...")
                time.sleep(2)
        except pyautogui.ImageNotFoundException:
            print("Login button image not found, retrying in 2 seconds...")
            time.sleep(2)
    time.sleep(1)

    # 로그인 후 추가 작업 수행 (필요에 따라)
    # driver.get("https://example.com/your_profile_page")  # 필요한 URL로 바꿔주세요

finally:
    # 완료 후 브라우저 닫기 (필요시)
    pass  # 필요시 driver.quit()으로 변경하세요
