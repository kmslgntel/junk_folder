import pyautogui
import time
import subprocess

# 스토브 클라이언트 실행
subprocess.Popen("C:\\Program Files (x86)\\STOVE\\STOVE.exe")
time.sleep(10)  # 클라이언트가 완전히 실행될 때까지 대기

# 특정 위치에 시작 버튼이 있는 경우 해당 좌표로 이동하여 클릭
# 좌표는 실제 화면에서 확인 후 변경 필요
start_button_x = 100  # 예시 좌표
start_button_y = 200  # 예시 좌표

# 시작 버튼 클릭
pyautogui.click(start_button_x, start_button_y)

print("스토브 클라이언트 실행 후 시작 버튼을 클릭했습니다.")
