from cryptography.fernet import Fernet
import os


def get_current_directory():
    return os.path.dirname(os.path.abspath(__file__))

current_path = get_current_directory()
key_path = os.path.join(current_path, "secret.key")

# 키 생성 및 저장
def generate_key():
    key = Fernet.generate_key()
    
    with open(key_path, "wb") as key_file:
        key_file.write(key)

# 키 로드
def load_key():
    return open(key_path, "rb").read()

# 메시지 암호화
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# 메시지 복호화
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message
