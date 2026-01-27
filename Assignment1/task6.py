import math
#nhập số liệu
talents=float(input("Nhập số talent: "))
pound = float(input("Nhập số pound: "))
lot =float(input("Nhập số lot: "))
#bắt đầu bước chuyển đổi
pound_to_lot = pound*32
talents_to_lot = talents*32*20
total_lot=pound_to_lot + talents_to_lot+lot
total_grams=total_lot*13.3
kilograms= int((total_lot)//1000)
grams= total_grams % 1000
# In kết quả
print(f"\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")
