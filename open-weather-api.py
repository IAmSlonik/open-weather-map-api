import requests

def check_weather(city):
    key = '44e36513b9809ae61bd8591de1811f12'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'

    response = requests.get(url)
    weatherMain = response.json()['weather'][0]['main']
    weatherDesc = response.json()['weather'][0]['description']

    mainTemp = response.json()['main']['temp']
    mainPress = response.json()['main']['pressure']
    mainHumi = response.json()['main']['humidity']

    windSpeed = response.json()['wind']['speed']
    windDeg = response.json()['wind']['deg']
    
    print(f'{city.upper()}:\n Weather: {weatherMain}, {weatherDesc}\n Temp: {mainTemp}°K,\n Pressure: {mainPress} hPa,\n Humidity: {mainHumi}%,\n Wind speed: {windSpeed} m/s,\n Wind degrees: {windDeg}°.')

city = input("Enter the city name: ")
check_weather(city)
