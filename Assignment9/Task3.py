import os

def convert_to_uppercase(input_filename, output_filename):
    # Lấy đường dẫn thư mục hiện tại của file code
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, input_filename)
    output_path = os.path.join(current_dir, output_filename)

    try:
        # Mở file đọc và file ghi cùng lúc
        with open(input_path, "r", encoding="utf-8") as f_in:
            with open(output_path, "w", encoding="utf-8") as f_out:
                for line in f_in:
                    # Chuyển từng dòng thành chữ hoa rồi ghi ngay vào file mới
                    f_out.write(line.upper())
        print(f"Đã chuyển đổi xong! Kiểm tra file: {output_filename}")
    
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file đầu vào {input_filename}")

convert_to_uppercase("Test.txt", "Product.txt")