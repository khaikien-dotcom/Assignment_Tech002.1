#task 1 check chiều dài con cá zender
def check_zander_size(length_cm):
    return length_cm >= 42, 42 - length_cm

length = float(input("Con cá mà bạn câu được dài bao nhiêu cm: "))
print(f"\nCon cá mà bạn câu được: {length:.1f} cm")

ok, diff = check_zander_size(length)

if ok:
    print("Con cá Zander của bạn đã đạt đủ kích thước.")
else:
    print("Vui lòng thả cá về hồ!")
    print(f"Thiếu {diff:.1f} cm.")

#task 2: phân loại tàu cabin
def cabin(classify_cabin):

    classify_cabin = classify_cabin.strip().upper()

    if classify_cabin == "LUX":
        return "Cabin hạng LUX của quý khách nằm ở tầng trên và có ban công."
    elif classify_cabin == "A":
        return "Cabin hạng A của quý khách nằm trên boong xe và được trang bị cửa sổ."
    elif classify_cabin == "B":
        return "Cabin hạng B của quý khách nằm trên boong xe và không có cửa sổ."
    elif classify_cabin == "C":
        return "Cabin hạng C của quý khách nằm dưới boong xe và không có cửa sổ."
    else:
        return "Hạng cabin không hợp lệ."


cabin_level = input("Nhập hạng cabin (LUX/A/B/C): ")
print(cabin(cabin_level))  # gọi hàm và in kết quả.

#task 3: kiểm tra hemo từng giới tính
def Check_hemoglobin():
  #nhập giới tính
    gender=input("cho tôi hỏi giới tính của bạn là gì (Male/Female):  ").lower()
#nhập giá trị hemo
    hemoglobin=float(input("mời bạn khai báo chỉ số hemoglobin (g/l) : "))
#Kiểm tra giới tính
    if gender=="male":
#Mức bình thường của Nam ở giữa: 134-167 g/l.
        if hemoglobin<134:
            print("Thấp")
        elif hemoglobin>167:
            print("cao")
        else:
            print("bình thường")
    elif gender=="female":
#Mức bình thường của Nữ ở giữa: 117 – 155 g/l
        if hemoglobin<117:
            print("thấp")
        elif hemoglobin>155:
            print("cao")
        else:
            print("bình thường")
    else:
        print("giới tính của bạn không phù hợp, Vui lòng bạn khai báo 'Male', 'Female' một cách chính xác.")

Check_hemoglobin()

#task 4
#nhập số liệu trước
def check_năm_nhuận(year):
#viết điều kiện của hàm
    if (year % 400 ==0) or (year % 4 ==0) and (year %100 !=0):
        print(f"Năm {year} của bạn là năm nhuận !")
    else:
        print(f"năm {year} của bạn không phải là năm nhuận")
#gọi hàm để xem kết quả
year=int(input("hãy cho tôi biết năm mà bạn muốn kiểm tra: "))
check_năm_nhuận(year)

#task 5
import math
def pizza_unit_price(diemeter,price_USD):
#diemeter: đường kính chiếc pizza(cm), price_USD: giá tiền chiếc pizza
#radius là bán kính hình tròn
    radius= diemeter/2
#diện tích hình tròn là A= π × r²
    area_cm2 = math.pi*radius**2
#bước chuyển đổi từ cm**2 sang m**2 (1m²=10,000cm²)
    area_m2= area_cm2/10000
#bước tính giá tiền của chiếc pizza
    pizza_price = price_USD / area_m2
    return pizza_price

def main():
    print(f"\nXin quý khách đưa ra lựa chọn thật kĩ càng! ")
    #nhập thông tin 2 chiếc pizza

print("pizza1:")
diemeter1=float(input("Khách hàng muốn chiếc pizza1 với đường kính(cm): "))
price_USD1=float(input("Giá tiền tính theo bảng quy đổi của cửa hàng(USD):"))

print("pizza2: ")
diemeter2=float(input("khách hàng muốn chiếc pizza2 với đường kính(cm): "))
price_USD2=float(input("Giá tiền tính theo bảng quy đổi của cửa hàng là(USD): "))
    
    #tính giá trị đơn vị cho cả 2 chiếc pizza
final_price_pizza1= pizza_unit_price(diemeter1,price_USD1)
final_price_pizza2= pizza_unit_price(diemeter2,price_USD2)

    #bước hiển thị kết quả sau khi nhập số liệu
print(f"\nTổng tiền của cả 2 chiếc pizza như sau:")
print(f"Chiếc pizza đầu tiên của bạn có giá: {final_price_pizza1:.1f}/m2 ")
print(f"Chiếc pizza thứ hai của bạn có giá: {final_price_pizza2:.1f}/m2 ")
    #bước so sánh và thông báo giá trị của pizza nào tốt hơn
if final_price_pizza1<final_price_pizza2:
    print("Chiếc pizza thứ 1 mà quý khách chọn rẻ hơn cái thứ 2.")
elif final_price_pizza2<final_price_pizza1:
    print("Chiếc pizza thứ 2 mà quý khách chọn rẻ hơn chiếc pizza thứ 1.")
else:
    print("giá trị của 2 chiếc pizza là tương đương nhau nên quý khách chọn cái nào cũng được!")

#gọi hàm 
main()
