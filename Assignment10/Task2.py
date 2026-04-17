import requests

API_KEY = "bd18d50034614898e62fbd155f1dc74c"
city = input("Nhập tên thành phố: ")  # Thêm input để nhập tên thành phố

# Lấy tọa độ từ tên thành phố
geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
geo_response = requests.get(geo_url)
geo_data = geo_response.json()

if geo_data:
    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]

    # Lấy thông tin thời tiết
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,  # Sửa thành API_KEY
        "units": "metric"
    }

    weather_response = requests.get(weather_url, params=params)
    weather_data = weather_response.json()

    description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]

    print("Weather:", description)
    print("Temperature:", temperature, "°C")

else:
    print("City not found")