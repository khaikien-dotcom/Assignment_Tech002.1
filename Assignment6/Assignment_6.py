#Task 1
numbers = []
while True: 
    user_num = input("Mời bạn nhập 1 dãy số(Enter để thoát): ")
    #Người dùng không nhập gì hết thì tự động thoát vòng lặp
    if user_num == "" :
        break
    numbers.append(float(user_num))
#Sắp xếp số theo thứ tự giảm dần
numbers.sort(reverse = True) 
first_5 = numbers[:5]
print("5 số lớn nhất bạn đã nhập: ", first_5)

#Task 2 
#Lưu các mùa vào tuple
seasons = ("Spring", "Summer","Autumn", "winter")
month = int(input("Mời bạn nhập tháng(1-12): "))
#xác định mùa dựa theo tháng
if month == 12 or month == 1 or month == 2:
    season = seasons[3]
elif month == 3  or month == 4 or month == 5:
    season = seasons[0]
elif month == 6 or month == 7 or month == 8:
    season = seasons[1]
elif month == 9 or month == 10 or month == 11:
    season = seasons[2]
else: 
    season = None
    print("Không xác định được tháng của bạn!")
print(f"\n tháng {month} của bạn nằm trong mùa {season}")

#Task 3 
names = set()
while True: 
    name = input("Mời bạn nhập tên: ")
    if names == "": 
        break
    #Kiểm tra tên có trong list
    elif name in names:
        print("Existing Name!")
    else:
        print("New Name!")
        names.add(name)
print("\nDanh sách tên đã nhập")
for n in names:
    print(n)