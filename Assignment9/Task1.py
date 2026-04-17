import os

def count_lines(filepath):
    # 1. Lấy thư mục chứa file code hiện tại
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_dir, filepath)
    
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            dem = 0
            for line in f:
                if line.strip():
                    dem += 1
            return dem
    except FileNotFoundError:
        return f"Lỗi: Không tìm thấy file tại {full_path}!"

ket_qua = count_lines('Test.txt')
print(f"Số dòng có nội dung: {ket_qua}")