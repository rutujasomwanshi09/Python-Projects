import requests

api_key = 'API KEY'

user_input = input("Enter your city: ")

url = (f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

response = requests.get(url)

data = response.json()


if response.json()['cod'] == '404':
    print("No City Found")
else:

    # weather = weather_data.json()['weather'][0]['main']
    # temp = round(weather_data.json()['main']['temp']['humidity'])
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind_speed = data["wind"]["speed"]

print(f"The weather in {user_input} is: {weather}")
print(f"The temperature in {user_input} is: {temp} °C")
print(f"The humidity in {user_input} is: {humidity} %")
print(f"The pressure in {user_input} is: {pressure} hPa")
print(f"The wind speed in {user_input} is: {wind_speed} m/s")