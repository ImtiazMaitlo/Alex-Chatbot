# import requests
# city=input("Enter City Name : ")
# url=f"123c5810624c48ea8e252404240203 = {city}"
# r=request.get(url)
# print(r.text)





import requests
import json 

api_key = 'ac5bc8ca58e74955ac054335240203'
base_url = 'https://www.weatherapi.com/my/#'

# Sindh coordinates (latitude, longitude)
sindh_coords = '24.8607,67.0011'

complete_url = f'{base_url}lat={sindh_coords[0]}&lon={sindh_coords[1]}&appid={api_key}'

response = requests.get(complete_url)
data = response.json()

print(data)  # Print the entire JSON response to inspect its structure

# Now, access the "main" key if it exists
if "main" in data:
    main_data = data["main"]
    temperature = main_data["temp"]
    pressure = main_data["pressure"]
    humidity = main_data["humidity"]
    weather_description = data["weather"][0]["description"]
    print(f"Temperature: {temperature}K")
    print(f"Pressure: {pressure}hPa")
    print(f"Humidity: {humidity}%")
    print(f"Weather Description: {weather_description}")
else:
    print("Main key not found in the response")


