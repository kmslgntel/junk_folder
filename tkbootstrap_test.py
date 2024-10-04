import os
import time
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# 기본 창 설정
root = ttk.Window(themename="darkly")  # darkly 테마 적용
root.title("파일 처리 진행 상태")
root.geometry("400x200")

# SUCCESS 스타일이 적용된 레이블
label = ttk.Label(root, text="폴더에서 파일을 처리 중...", font=("Helvetica", 14))
label.pack(pady=10)

# SUCCESS 스타일이 적용된 프로그레스바
progressbar = ttk.Progressbar(root, bootstyle="success", length=300, mode='determinate')
progressbar.pack(pady=20)

# 파일을 처리하는 함수
def process_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    total_files = len(files)
    progressbar['maximum'] = total_files  # 프로그레스바 최대값 설정
    
    for i, file in enumerate(files):
        file_path = os.path.join(folder_path, file)
        # 파일 처리 로직 (여기서는 파일 이름을 출력하는 것으로 대체)
        print(f"Processing file: {file_path}")
        
        # 처리 시 약간의 지연을 추가
        time.sleep(0.2)
        
        # 처리 완료 후 프로그레스바 값 증가
        progressbar['value'] = i + 1
        root.update_idletasks()  # 프로그레스바 업데이트

# 파일 처리 시작 버튼을 클릭할 때 호출되는 함수
def start_processing():
    folder_path = "D:/home/value_extraction/data_collection_240805/excel_file"  # 처리할 폴더 경로를 지정
    process_files_in_folder(folder_path)

# SUCCESS 스타일이 적용된 버튼
button = ttk.Button(root, text="파일 처리 시작", bootstyle="success", command=start_processing)
button.pack(pady=10)

# 메인 루프 실행
root.mainloop()
