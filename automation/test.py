import psutil
import os

# 시스템에 연결된 드라이브 목록 가져오기
def get_usb_drives():
    drives = []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        if 'removable' in partition.opts:  # USB 드라이브를 필터링
            drives.append(partition.device)
    return drives

# USB 드라이브 목록 출력 및 선택
usb_drives = get_usb_drives()

if not usb_drives:
    print("USB 드라이브가 연결되지 않았습니다.")
else:
    print("다음 USB 드라이브가 연결되어 있습니다:")
    for idx, drive in enumerate(usb_drives):
        print(f"{idx + 1}. {drive}")

    # 사용자에게 드라이브 선택 요청
    selected_drive_index = int(input("사용할 USB 드라이브 번호를 입력하세요: ")) - 1
    selected_drive = usb_drives[selected_drive_index]

    if os.path.exists(selected_drive) and os.path.isdir(selected_drive):
        print(f"선택된 USB 드라이브: {selected_drive}")
    else:
        print("선택한 드라이브가 유효하지 않습니다.")
