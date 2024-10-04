import PyPDF2
import itertools
import string

def try_password(pdf_reader, password):
    if pdf_reader.decrypt(password) == 1:
        print(f"Password found: {password}")
        return password
    return None

def brute_force_pdf(pdf_file, max_length):
    with open(pdf_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        
        if not pdf_reader.is_encrypted:
            print("The PDF file is not encrypted.")
            return
        
        chars = string.ascii_letters + string.digits + string.punctuation
        total_attempts = sum(len(chars) ** length for length in range(1, max_length + 1))
        print(f"Total password combinations to try: {total_attempts}")

        attempts = itertools.chain.from_iterable(
            itertools.product(chars, repeat=length) for length in range(1, max_length + 1)
        )
        
        attempt_count = 0
        for attempt in attempts:
            password = ''.join(attempt)
            attempt_count += 1
            result = try_password(pdf_reader, password)
            if attempt_count % 100 == 0:
                print(f"Attempts: {attempt_count}/{total_attempts}")
            if result:
                print(f"Password found: {result}")
                return True

        print("Password not found.")
        return False

# 파일 경로와 시도할 비밀번호의 최대 길이를 지정합니다.
pdf_file = "D:/김명섭/신지혜_경력_이력서.pdf"
max_length = 8  # 8글자까지 시도

brute_force_pdf(pdf_file, max_length)
