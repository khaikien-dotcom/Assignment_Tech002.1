import os

def find_keyword_lines(filename, keyword):
    line_numbers = []
    
    # Lấy đường dẫn tuyệt đối để tránh lỗi FileNotFoundError
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_dir, filename)

    try:
        with open(full_path, "r", encoding="utf-8") as file:
            for index, line in enumerate(file, start=1):
                if keyword in line:
                    line_numbers.append(index)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {filename} tại {full_path}")
        return []

    return line_numbers

# Chạy thử
ket_qua = find_keyword_lines("Test.txt", "God_of_war")
print(f"Từ khóa xuất hiện tại các dòng: {ket_qua}")