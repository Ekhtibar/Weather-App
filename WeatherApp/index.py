import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

root = tb.Window(themename='darkly')
root.geometry('1200x650')

style = tb.Style()

style.configure('left_side.TFrame', background="#222222")
left_side = ttk.Frame(root, style='left_side.TFrame', padding=(45, 65))
style.configure('right_side.TFrame', background="#fff")
right_side = ttk.Frame(root, style='right_side.TFrame')

left_side.grid(row=0, column=0, sticky="nsew")
right_side.grid(row=0, column=1, sticky="nsew")

root.grid_columnconfigure(0, weight=65) 
root.grid_columnconfigure(1, weight=35)  

hero_city_and_weather_status = ttk.Frame(left_side)
hero_city_and_weather_status.pack(side=tk.LEFT, fill=tk.NONE, anchor='n', expand=False)

hero_current_city = tb.Label(hero_city_and_weather_status, text="Тамбов", font=("Roboto", 16))
hero_current_city.pack(side=tk.LEFT, fill=tk.NONE, anchor='nw', expand=False)

weather_status_label = tb.Label(left_side, text="Облачно", bootstyle="danger, inverse")
weather_status_label.pack(side=tk.LEFT)

# Заполняем правую сторону
right_label = tb.Label(right_side, text="Right Side", font=("Roboto", 16))
right_label.pack(pady=20)

display_label = tb.Label(right_side, text="")
display_label.pack(pady=20)

# Запускаем главный цикл приложения
root.mainloop()