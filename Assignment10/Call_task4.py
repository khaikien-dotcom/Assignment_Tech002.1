import requests
import json

def get_airport_data():
    icao = input("Nhập mã ICAO của sân bay (VD: LFLL, EGLL): ").strip()
    
    url = f"http://127.0.0.1:5000/airport/{icao}"
    
    try:
        response = requests.get(url)
        
        # Kiểm tra xem yêu cầu có thành công hay không (Status code 200)
        if response.status_code == 200:
            data = response.json()
            print("\n--- Thông tin sân bay ---")
            print(json.dumps(data, indent=4))
        elif response.status_code == 404:
            print(f"\nLỗi: Không tìm thấy sân bay với mã '{icao}'")
        else:
            print(f"\nLỗi hệ thống: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("\nLỗi: Không thể kết nối tới Server. Hãy đảm bảo server.py đang chạy!")

if __name__ == '__main__':
    get_airport_data()