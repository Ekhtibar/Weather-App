import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from PIL import Image, ImageTk


class WeatherDetail(tk.Frame):
    def __init__(self, parent, style, wind_image_path, wind_speed, humidity_image_path, humidity_value, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Создаем общий Frame для скорости ветра и влажности
        frame_weather = tk.Frame(self)
        frame_weather.pack(side=tk.TOP,fill=tk.Y, anchor='nw')

        # wind speed
        frame_wind_speed = tk.Frame(frame_weather)  
        frame_wind_speed.pack(side=tk.LEFT, fill=tk.Y, anchor='nw')

        wind_speed_image = ImageTk.PhotoImage(Image.open(wind_image_path))
        wind_speed_image_label = ttk.Label(frame_wind_speed, image=wind_speed_image)
        wind_speed_image_label.image = wind_speed_image  # Сохраняем ссылку на изображение
        wind_speed_image_label.pack(side=tk.LEFT, fill=tk.Y, anchor='nw')

        # wind_speed_value
        style.configure('WindSpeed.TLabel', foreground='#A5A5A5')
        wind_speed_value = ttk.Label(frame_wind_speed, text=f"{wind_speed} м/с", font=("Roboto", 10), style='WindSpeed.TLabel')
        wind_speed_value.pack(side=tk.LEFT, fill=tk.Y)

        # humidity
        frame_humidity = tk.Frame(frame_weather)  
        frame_humidity.pack(side=tk.LEFT, padx=20, fill=tk.Y, anchor='nw', expand=True) 

        humidity_image = ImageTk.PhotoImage(Image.open(humidity_image_path))
        humidity_image_label = ttk.Label(frame_humidity, image=humidity_image)
        humidity_image_label.image = humidity_image  # Сохраняем ссылку на изображение
        humidity_image_label.pack(side=tk.LEFT,  fill=tk.Y, anchor='nw', expand=True)

        # humidity_value
        style.configure('Humidity.TLabel', foreground='#A5A5A5')
        humidity_value_label = ttk.Label(frame_humidity, text=f"{humidity_value}%", font=("Roboto", 10), style='Humidity.TLabel')
        humidity_value_label.pack(side=tk.LEFT, fill=tk.Y, anchor='nw')