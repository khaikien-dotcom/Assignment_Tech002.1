import re
#===================task 1=================
def valid_course_code(code):
    if len(code) !=6:
        return False
    if not code[:3].isalpha() or not code[:3].isupper():
        return False
    if not code[3:].isdigit():
        return False
    return True

course_code = input("Mời bạn nhập mã môn học: ")
if valid_course_code(course_code):
    print("Đã xác nhận mã môn học của bạn!")
else:
    print("Không xác nhận được mã môn học của bạn!")

#=================task2================
def valid_hex_color(color):
    #kiểm tra độ dài và ký tự đầu
    if len(color) !=7 or color[0] != "#":
        return False
    #kiểm tra 6 ký tự phía sau
    hex_num = color[1:]
    #Kiểm tra từng ký tự
    for char in hex_num:
        if not (char.isdigit() or char.lower() in "abcdef"):
            return False
    return True
color_code = input("Mời bạn nhập mã màu hex: ")
if valid_hex_color(color_code):
    print("mã màu của bạn hợp lệ!")
else:
    print("Mã màu của bạn không hợp lệ!")

#==================task3==============
def sum_num_in_text(text):
    #tìm các chuỗi số trong đoạn văn bản
    numbers = re.findall(r'\d+', text)
    #Chuyển từng chuỗi số thành số nguyên và tính tổng
    total = sum(int(num) for num in numbers)
    return total
#Nhập văn bản
paragraph = input("Mời bạn nhập văn bản:")
result = sum_num_in_text(paragraph)
print("Tổng các số tìm được: ", result)

#===================task4================
def redact_phone_numbers(text):
    pattern = r'(\b\d{10}\b|\+84\d+)'
# Pattern:
#\b: Đảm bảo không dính với số khác
#\d: Chữ số
#\+84 Bắt đầu bằng +84
#\d+: Nhiều chữ số trở lên
    result = re.sub(pattern, '[REDACTED]', text)
#re.sub(pattern, replacement, string)
    return result
document = input("Yêu cầu bạn nhập văn bản:")
#Ẩn số điện thoại
hidden_num = redact_phone_numbers(document)
print("Sau khi ẩn ố điện thoại:")
print(hidden_num)

#==================end================

