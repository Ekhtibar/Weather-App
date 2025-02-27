import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from PIL import Image, ImageTk


class WeatherByDay:
    def __init__(self, parent, style, weather_data):
        self.parent = parent
        self.style = style
        self.weather_data = weather_data
        self.create_weather_display()

    def create_weather_display(self):
        self.style.configure('DarFrame.TFrame', background="#333333")
        self.style.configure('DayItem.TLabel', background="#333333", foreground="#FFFFFF")
        
        columns = [ttk.Frame(self.parent, width=150) for _ in range(3)]
        for column in columns:
            column.pack(side=tk.LEFT, fill=tk.Y)

        for i, data in enumerate(self.weather_data):
            column_index = i % 3 
            column = columns[column_index]

            frame = ttk.Frame(column, style='DarFrame.TFrame', padding=10)
            frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

            weather_icon = ImageTk.PhotoImage(Image.open(data["icon_path"]))
            weather_icon_label = ttk.Label(frame, image=weather_icon, style='DayItem.TLabel')
            weather_icon_label.image = weather_icon
            weather_icon_label.pack(side=tk.LEFT, fill=tk.X, anchor='center', expand=False)

            label = ttk.Label(frame, text=f"{data['day']}: {data['temperature']}", background="#333333", foreground="white", font=("Roboto", 10))
            label.pack(side=tk.TOP, anchor='nw', padx=5)

            weather_txt_label = ttk.Label(frame, text=data["condition"], background="#375A7F", foreground="white", font=("Roboto", 8))
            weather_txt_label.pack(side=tk.TOP, anchor='nw', padx=5, pady=(5, 0))