import pyautogui
import time

print("5초 후에 현재 마우스 위치를 출력합니다. 시작 버튼 위에 마우스를 올려놓으세요.")
time.sleep(5)

current_mouse_x, current_mouse_y = pyautogui.position()
print(f"현재 마우스 위치: X={current_mouse_x}, Y={current_mouse_y}")
