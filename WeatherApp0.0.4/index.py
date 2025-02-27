import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from PIL import Image, ImageTk
from win10toast import ToastNotifier 
import webbrowser
import requests
import json

# Components
from component.WeatherHeroDetail import WeatherDetail
from component.WeatherByHours import WeatherByHour
from component.WeatherByDay import WeatherByDay
from component.WeatherCities import WeatherCities

# Models
from models.getCurrentOnceWeather import CurrentWeatherMainLocation 
from models.getWeatherHourly import GetWeatherByHourly


weather_data = [
    {"day": "Вчера", "temperature": "-15", "condition": "Облачно", "icon_path": r'assets\bhci_ic.png'},
    {"day": "Сегодня", "temperature": "-26", "condition": "Облачно", "icon_path": r'assets\bhci_ic.png'},
    {"day": "Завтра", "temperature": "-15", "condition": "Облачно", "icon_path": r'assets\bhci_ic.png'},
    {"day": "Пн", "temperature": "-15", "condition": "Облачно", "icon_path": r'assets\bhci_ic.png'},
    {"day": "Вт", "temperature": "-15", "condition": "Облачно", "icon_path": r'assets\bhci_ic.png'},
    {"day": "Ср", "temperature": "-15", "condition": "Облачно", "icon_path": r'assets\bhci_ic.png'},
]


cities_data = [
    {"name": "Москва", "temperature": "-5°-0°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Санкт-Петербург", "temperature": "-3°-2°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    {"name": "Новосибирск", "temperature": "-10°-5°", "icon_path": r'assets\city_weather_ic.png'},
    
]


root = tb.Window(themename='darkly')
root.title("Погода ТГТУ")
root.geometry('1200x850')
root.resizable(False, False)

style = tb.Style()

style.configure('left_side.TFrame', background="#222222")
left_side = ttk.Frame(root, style='left_side.TFrame', padding=(40, 35))
style.configure('right_side.TFrame', background="#222222")
right_side = ttk.Frame(root, style='right_side.TFrame')

left_side.grid(row=0, column=0, sticky="nsew")
right_side.grid(row=0, column=1, sticky="nsew")

root.grid_columnconfigure(0) 
root.grid_columnconfigure(1, weight=35)

hero_city_and_weather_status = ttk.Frame(left_side)
hero_city_and_weather_status.pack(side=tk.LEFT, fill=tk.NONE, anchor='n', expand=False)

hero_app_name = ttk.Label(hero_city_and_weather_status, text="ТГТУ МетеоСервис", font=("Roboto", 22))
hero_app_name.pack(side=tk.TOP, fill=tk.NONE, anchor='nw', expand=False)

hero_current_city = ttk.Label(hero_city_and_weather_status, text="Тамбов", font=("Roboto", 16))
hero_current_city.pack(side=tk.TOP, fill=tk.NONE, pady=(35, 0), anchor='nw', expand=False)

api_key = "b2ea9c54-9867-486a-a3a4-05a1c9656275" 
lat = 52.71833
lon = 41.43333

current_city_weather = CurrentWeatherMainLocation(api_key, lat, lon)

current_weather_data = current_city_weather.get_weather() 

current_weather_filename = './data/current_city_weather_data.json'
if current_weather_data:
    current_city_weather.save_weather_to_json(current_weather_filename)

current_city_weather_data = current_city_weather.load_weather_from_json(current_weather_filename)

if current_city_weather_data:
    temperature = current_city_weather_data['temperature']
    condition = current_city_weather_data['condition']
    
    day_date = ttk.Label(hero_city_and_weather_status, text="Сегодня, 18 февраля", font=("Roboto", 10))
    day_date.pack(side=tk.TOP, fill=tk.NONE, anchor='nw', expand=False)

    weather_status_label = tb.Label(hero_city_and_weather_status, text=condition, bootstyle="secondary, inverse, CustomInverse.TLabel")
    weather_status_label.pack(side=tk.TOP, pady=5, anchor='nw', expand=False)

    temperature_frame = ttk.Frame(hero_city_and_weather_status)
    temperature_frame.pack(side=tk.TOP, fill=tk.X, anchor='nw', expand=False)

    weather_temperature = ttk.Label(temperature_frame, text=f"{temperature}°C", font=("Roboto", 48))
    weather_temperature.pack(side=tk.LEFT, pady=17, anchor='n', expand=False)

    icon_path = current_city_weather.get_weather_icon(condition)
    original_image = Image.open(icon_path)
    resized_image = original_image.resize((100, 100))

    current_weather_img = ImageTk.PhotoImage(resized_image)
    current_weather_img_label = ttk.Label(temperature_frame, image=current_weather_img)
    current_weather_img_label.image = current_weather_img 
    current_weather_img_label.pack(side=tk.LEFT, padx=20, fill=tk.X, anchor='nw', expand=False)

    wind_speed = current_city_weather_data['windSpeed']
    humidity = current_city_weather_data['humidity']

    # Создаем компонент WeatherDetail
    weather_detail = WeatherDetail(
        hero_city_and_weather_status,
        style,
        r'./assets/wind.png',  
        wind_speed,  
        r'./assets/humidity.png', 
        humidity  
    )
    weather_detail.pack(side=tk.TOP, anchor='nw')
else:
    print("Не удалось загрузить данные о текущей погоде.")

# weather by hour title
by_hour_label = ttk.Label(hero_city_and_weather_status, text="По часам", font=("Roboto", 10), style="by_hour_label.TLabel")
by_hour_label.pack(side=tk.TOP, anchor='sw', pady=(35, 15), expand=False)

hourly_weather = GetWeatherByHourly(api_key, lat, lon)
hourly_data_filename = './data/hourly_weather_data.json'
hourly_weather_data = hourly_weather.get_hourly_weather()

if hourly_weather_data:
    with open(hourly_data_filename, 'w', encoding='utf-8') as json_file:
        json.dump(hourly_weather_data, json_file, ensure_ascii=False, indent=4)
    print("Hourly weather data saved to hourly_weather_data.json")

hourly_weather_data = hourly_weather.load_weather_from_json(hourly_data_filename)

# Создаем компонент WeatherByHour 
if hourly_weather_data: 
    weather_by_hour = WeatherByHour(
        hero_city_and_weather_status, 
        tb.Style(), 
        hourly_weather_data,
        r"./assets/left_arrow_btn.png", 
        r"./assets/right_arrow_btn.png"
    )
    weather_by_hour.pack(side=tk.TOP, fill=tk.X, anchor='nw', expand=False)

# title WeatherByDay
by_day_label = ttk.Label(hero_city_and_weather_status, text="По дням", font=("Roboto", 10), style="by_hour_label.TLabel")
by_day_label.pack(side=tk.TOP, anchor='sw', pady=(35, 10), expand=False)

# create component WeatherByDay
weather_by_day = WeatherByDay(hero_city_and_weather_status, style, weather_data)

# START SEARCH
def on_submit():
    user_input = entry.get()
    print(f"Вы ввели: {user_input}")


right_label = ttk.Label(right_side, text="Поиск по городам", font=("Roboto", 12))
right_label.pack(pady=(45, 0), padx=(0, 35), side=tk.TOP, anchor='nw')

entry_frame = ttk.Frame(right_side, width=350)
entry_frame.pack(side=tk.TOP, anchor='ne', fill=tk.X, pady=10)

entry = ttk.Entry(entry_frame, width=35)
entry.pack(side=tk.LEFT, fill=tk.X, expand=False)

submit_button = ttk.Button(entry_frame, text="Отправить", command=on_submit, takefocus=False)
submit_button.pack(side=tk.LEFT, padx=(0, 35))
# END SEARCH

style.configure('cityWeatherItem.TFrame', background="#333333")
style.configure('removeBgLabel.TLabel', background="#333333", foreground="#FFFFFF")

weather_cities = WeatherCities(right_side)
weather_cities.populate_weather_items(cities_data)



root.mainloop()