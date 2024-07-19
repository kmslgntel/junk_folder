from encrypt_decrypt import generate_key, encrypt_message
import os
import getpass

def get_current_directory():
    return os.path.dirname(os.path.abspath(__file__))

current_path = get_current_directory()
credentials_path = os.path.join(current_path, "credentials.enc")

# 처음 한 번만 키 생성
generate_key()

# 사용자 정보 설정
username = input("ID : ")
password = getpass.getpass("PW: ")
# 사용자 정보 암호화
encrypted_username = encrypt_message(username)
encrypted_password = encrypt_message(password)

# 암호화된 사용자 정보 파일에 저장
with open(credentials_path, "wb") as file:
    file.write(encrypted_username + b"\n" + encrypted_password)
