from encrypt_decrypt import decrypt_message
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
import time
import os

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

# Chrome 디버깅 옵션 설정
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# 잠시 대기 (Chrome이 완전히 시작될 시간을 줍니다)
time.sleep(5)

# 웹드라이버 설정 및 기존 Chrome 창 연결
driver = None
while driver is None:
    try:
        # 웹드라이버 설정 및 기존 Chrome 창 연결
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        print("Driver connected successfully.")
    except WebDriverException as e:
        print(f"Driver connection failed: {e}")
        print("Retrying in 10 seconds...")
        time.sleep(5)  # 10초 간격으로 재시도

try:
    # 로그인 페이지로 이동
    driver.get("https://gw.lgntel.com/Account/Login2")  # 여기에 로그인 페이지 URL을 입력하세요

    # 사용자 이름 입력
    username_field = driver.find_element(By.ID, "UserName")  # 실제 ID로 바꿔주세요
    username_field.send_keys(username)

    # 비밀번호 입력
    password_field = driver.find_element(By.ID, "Password")  # 실제 ID로 바꿔주세요
    password_field.send_keys(password)

    # 로그인 버튼 클릭 (XPath 사용 예제)
    login_button = driver.find_element(By.XPATH, "//*[@id='login_content']/form/div/div[1]/a")
    login_button.click()

    # 로그인 후 추가 작업 수행 (필요에 따라)
    # driver.get("https://example.com/your_profile_page")  # 필요한 URL로 바꿔주세요

finally:
    # 완료 후 브라우저 닫기 (필요시)
    pass  # 필요시 driver.quit()으로 변경하세요
