import PyPDF2
import itertools

def try_password(pdf_reader, password):
    """
    Try decrypting the PDF file with the given password.
    
    :param pdf_reader: PyPDF2 PdfReader object
    :param password: Password to try
    :return: The password if successful, otherwise None
    """
    if pdf_reader.decrypt(password) == 1:
        return password
    return None

def generate_combinations(word_list, max_length):
    """
    Generate all possible combinations of words from the given word list,
    concatenated without spaces.
    
    :param word_list: List of words to combine
    :param max_length: Maximum number of words in each combination
    :return: Generator yielding each combination
    """
    for length in range(1, max_length + 1):
        for combination in itertools.permutations(word_list, length):
            yield ''.join(combination)  # Join words without spaces

def brute_force_pdf(pdf_file, word_list, max_length):
    """
    Attempt to decrypt the PDF file using combinations of words.
    
    :param pdf_file: Path to the PDF file
    :param word_list: List of words to combine
    :param max_length: Maximum number of words in each combination
    """
    with open(pdf_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        
        if not pdf_reader.is_encrypted:
            print("The PDF file is not encrypted.")
            return
        
        total_attempts = sum(len(word_list) ** length for length in range(1, max_length + 1))
        print(f"Total password combinations to try: {total_attempts}")

        attempt_count = 0
        found_password = None
        
        for password in generate_combinations(word_list, max_length):
            attempt_count += 1
            result = try_password(pdf_reader, password)
            
            if attempt_count % 100 == 0:
                print(f"Attempts: {attempt_count}/{total_attempts}")
            
            if result:
                print(f"Password found: {result}")
                return True
        
        print("Password not found.")
        return False

# 파일 경로와 단어 리스트, 최대 비밀번호 길이를 지정합니다.
pdf_file = "D:/김명섭/신지혜_경력_이력서.pdf"
word_list = ["lgntel", "gntel", "2024", "-", "_", "dlstk", "codyd", "!", "#", "@", "dkswjs", "vlvmf", "dkswjs&vlvmf", "big", "qordlsrl", "dlsrl", "djaxoal", "bobtong0124", "bobtong", "0124"]
max_length = 4  # 조합의 최대 길이

brute_force_pdf(pdf_file, word_list, max_length)
