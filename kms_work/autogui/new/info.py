import ttkbootstrap as ttk
from tkinter import messagebox, Listbox  # tkinter에서 Listbox 가져오기
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

# JSON 파일에 계정 정보 저장
def save_accounts(accounts):
    with open("accounts.json", "w") as file:
        json.dump(accounts, file)

# 계정 저장 함수
def save_account(username, password, fernet, listbox):
    accounts = load_accounts()
    if len(accounts) < 3:
        encrypted_username = encrypt_data(username, fernet)
        encrypted_password = encrypt_data(password, fernet)
        accounts.append({"username": encrypted_username, "password": encrypted_password})
        save_accounts(accounts)
        
        # Listbox에 실시간으로 새로운 계정 추가
        listbox.insert("end", username)
        
        messagebox.showinfo("Success", "Account saved successfully!")
    else:
        messagebox.showwarning("Limit Reached", "You can only save 3 accounts.")

# 계정 삭제 함수
def delete_account(selected_username, fernet, listbox):
    accounts = load_accounts()
    for account in accounts:
        if decrypt_data(account["username"], fernet) == selected_username:
            accounts.remove(account)
            save_accounts(accounts)
            messagebox.showinfo("Deleted", "Account has been deleted.")
            return
    messagebox.showerror("Error", "Account not found.")

# GUI 구성 함수
def create_gui():
    key = load_key()
    fernet = Fernet(key)

    root = ttk.Window(themename="darkly")
    root.title("Account Manager")
    
    ttk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
    username_entry = ttk.Entry(root)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    password_entry = ttk.Entry(root, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # 계정 저장 시 실시간 반영
    def save():
        username = username_entry.get()
        password = password_entry.get()
        if username and password:
            save_account(username, password, fernet, account_listbox)
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
        else:
            messagebox.showwarning("Input Error", "Please enter both username and password.")

    save_button = ttk.Button(root, text="Save Account", command=save)
    save_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Adding a delete functionality
    ttk.Label(root, text="Select Account to Delete:").grid(row=3, column=0, padx=10, pady=10)
    accounts = load_accounts()

    # tkinter의 Listbox 사용
    account_listbox = Listbox(root, height=3)
    for account in accounts:
        account_listbox.insert("end", decrypt_data(account["username"], fernet))
    account_listbox.grid(row=3, column=1, padx=10, pady=10)

    # 계정 삭제 시 실시간 반영
    def delete():
        selected_account = account_listbox.get(account_listbox.curselection())
        delete_account(selected_account, fernet, account_listbox)
        account_listbox.delete(account_listbox.curselection())

    delete_button = ttk.Button(root, text="Delete Account", command=delete)
    delete_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
