import os

def average_score(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_dir, filename)
    total = 0
    count = 0
    try:
        with open(full_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line: # Bỏ qua nếu là dòng trống
                    continue
                
                try:

                    parts = line.split(",")
                    if len(parts) == 2:
                        name = parts[0]
                        score = float(parts[1]) # Dùng float để tính được cả điểm lẻ (8.5)
                        total += score
                        count += 1
                except ValueError:
                    print(f"Bỏ qua dòng lỗi định dạng điểm: {line}")
                    
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file dữ liệu.")
        return 0
    return total / count if count > 0 else 0
print(f"Điểm trung bình là: {average_score('Scores.txt')}")