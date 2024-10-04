import tkinter as tk
from tkinter import messagebox
from pynput import mouse
import json
import os
from cryptography.fernet import Fernet

# 암호화를 위한 키 생성 (한 번 생성 후 저장하여 재사용)
key_path = "secret.key"
if not os.path.exists(key_path):
    key = Fernet.generate_key()
    with open(key_path, 'wb') as key_file:
        key_file.write(key)
else:
    with open(key_path, 'rb') as key_file:
        key = key_file.read()

cipher_suite = Fernet(key)

# 선택된 버튼과 라벨을 추적하기 위한 변수
selected_button = None
selected_label = None

# 좌표 데이터를 저장할 딕셔너리
coordinates = {
    "logo": {"x": 0, "y": 0},
    "id": {"x": 0, "y": 0},
    "pw": {"x": 0, "y": 0},
    "tab": {"x": 0, "y": 0},
    "start": {"x": 0, "y": 0}
}

# JSON 파일 경로
json_file_path = "coordinates.json"

def select_button(button, label, key):
    global selected_button, selected_label, selected_key
    selected_button = button
    selected_label = label
    selected_key = key

def on_click(x, y, button, pressed):
    global selected_button, selected_label, selected_key
    if pressed and selected_button:
        selected_label.config(text=f"({x}, {y})")
        coordinates[selected_key] = {"x": x, "y": y}
        selected_button = None  # 클릭 후 선택 해제
        selected_label = None

def save_coordinates():
    with open(json_file_path, 'w') as file:
        json.dump(coordinates, file)
    messagebox.showinfo("저장 완료", "좌표가 저장되었습니다.")

def load_coordinates():
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            return json.load(file)
    return coordinates

def save_credentials():
    id_data = id_entry.get()
    pw_data = pw_entry.get()
    encrypted_id = cipher_suite.encrypt(id_data.encode())
    encrypted_pw = cipher_suite.encrypt(pw_data.encode())
    with open("credentials.enc", 'wb') as enc_file:
        enc_file.write(encrypted_id + b'\n' + encrypted_pw)
    messagebox.showinfo("저장 완료", "ID와 PW가 암호화되어 저장되었습니다.")

def load_credentials():
    if os.path.exists("credentials.enc"):
        with open("credentials.enc", 'rb') as enc_file:
            encrypted_id, encrypted_pw = enc_file.read().split(b'\n')
            id_data = cipher_suite.decrypt(encrypted_id).decode()
            pw_data = cipher_suite.decrypt(encrypted_pw).decode()
            id_entry.insert(0, id_data)
            pw_entry.insert(0, pw_data)

# Tkinter 기본 윈도우 생성
root = tk.Tk()
root.title("Button Position")
root.geometry("300x550")

# 좌표 데이터 로드
coordinates = load_coordinates()

# 여러 개의 버튼과 라벨 생성
logo_button = tk.Button(root, text="로고_좌표", command=lambda: select_button(logo_button, logo_label, "logo"))
logo_button.pack(pady=5)
logo_label = tk.Label(root, text=f"({coordinates['logo']['x']}, {coordinates['logo']['y']})")
logo_label.pack(pady=5)

id_button = tk.Button(root, text="ID_좌표", command=lambda: select_button(id_button, id_label, "id"))
id_button.pack(pady=5)
id_label = tk.Label(root, text=f"({coordinates['id']['x']}, {coordinates['id']['y']})")
id_label.pack(pady=5)

pw_button = tk.Button(root, text="PW_좌표", command=lambda: select_button(pw_button, pw_label, "pw"))
pw_button.pack(pady=5)
pw_label = tk.Label(root, text=f"({coordinates['pw']['x']}, {coordinates['pw']['y']})")
pw_label.pack(pady=5)

tab_button = tk.Button(root, text="탭_좌표", command=lambda: select_button(tab_button, tab_label, "tab"))
tab_button.pack(pady=5)
tab_label = tk.Label(root, text=f"({coordinates['tab']['x']}, {coordinates['tab']['y']})")
tab_label.pack(pady=5)

start_button = tk.Button(root, text="시작_좌표", command=lambda: select_button(start_button, start_label, "start"))
start_button.pack(pady=5)
start_label = tk.Label(root, text=f"({coordinates['start']['x']}, {coordinates['start']['y']})")
start_label.pack(pady=5)

# 저장 버튼 생성
save_button = tk.Button(root, text="좌표 저장", command=save_coordinates)
save_button.pack(pady=5)


# ID와 PW 입력 필드 생성
tk.Label(root, text="ID:").pack(pady=5)
id_entry = tk.Entry(root)
id_entry.pack(pady=5)

tk.Label(root, text="PW:").pack(pady=5)
pw_entry = tk.Entry(root, show="*")
pw_entry.pack(pady=5)

save_credentials_button = tk.Button(root, text="ID/PW 저장", command=save_credentials)
save_credentials_button.pack(pady=5)

# 암호화된 자격 증명 로드
load_credentials()

# 마우스 리스너 설정
listener = mouse.Listener(on_click=on_click)
listener.start()

root.mainloop()
