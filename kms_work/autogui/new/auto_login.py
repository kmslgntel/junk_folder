from cryptography.fernet import Fernet
import json
import os

# 키 파일이 없을 때 키를 생성하고 저장하는 함수
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# 키 로드 함수 (키 파일이 없으면 생성 후 로드)
def load_key():
    if not os.path.exists("secret.key"):
        generate_key()
    return open("secret.key", "rb").read()

# 계정 정보를 암호화하는 함수
def encrypt_data(data, fernet):
    return fernet.encrypt(data.encode()).decode()

# 암호화된 계정 정보를 복호화하는 함수
def decrypt_data(encrypted_data, fernet):
    return fernet.decrypt(encrypted_data.encode()).decode()

# JSON 파일에서 계정 정보 로드
def load_accounts():
    try:
        with open("accounts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

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

# 콘솔에서 계정 선택 및 로그인 시도 함수
def select_account_for_login():
    key = load_key()
    fernet = Fernet(key)
    
    accounts = load_accounts()
    
    if not accounts:
        print("저장된 계정이 없습니다.")
        return

    print("로그인할 계정을 선택하세요:")
    for i, account in enumerate(accounts):
        username = decrypt_data(account["username"], fernet)
        print(f"{i + 1}. {username}")

    # 번호 선택 입력 받기
    selected = int(input("번호를 입력하세요: ")) - 1

    if selected < 0 or selected >= len(accounts):
        print("잘못된 선택입니다.")
        return

    # 선택된 계정의 정보 복호화
    selected_account = accounts[selected]
    username = decrypt_data(selected_account["username"], fernet)
    password = decrypt_data(selected_account["password"], fernet)
    
    # 여기서 로그인 시도
    print(f"선택된 계정으로 로그인 시도 중: {username}")
    #print(f"Password: {password}")
    
    stove_path = "C:\\Program Files (x86)\\STOVE\\STOVE.exe"

    stove_name = os.path.basename(stove_path)

    def is_stove_running(stove_name):
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == stove_name:
                return True
            return False

    # 스토브 클라이언트 실행
    if not is_stove_running(stove_name):
        subprocess.Popen(stove_path)
    time.sleep(10)  # 클라이언트가 완전히 실행될 때까지 대기

    # 자동화 시작
    #time.sleep(2)  # 시작 전에 2초 대기 (필요에 따라 조정)
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


    type_credentials(username, password)

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

if __name__ == "__main__":
    select_account_for_login()
