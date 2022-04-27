import requests
import datetime
from pprint import pprint
from config import open_weather_token

def get_weather(city, open_weather_token):
    try:
        #url = f"api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}"
        r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric&lang=ru")
        data = r.json()
        #pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        print(f"Погода в городе {city}\n{cur_weather} C\nВлажность {humidity}%\n"
            f"Атмосферное давление {pressure} мм. рт.ст\nСкорость ветра {wind} м/с\n"
            f"Восход солнца {sunrise}")


    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()