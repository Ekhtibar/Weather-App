import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class WeatherCities:
    def __init__(self, parent):
        self.parent = parent

        self.canvas = tk.Canvas(parent)
        self.scrollbar = ttk.Scrollbar(parent, orient="vertical", command=self.canvas.yview, takefocus=False)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.image_references = []

        self.canvas.bind("<MouseWheel>", self.on_mouse_wheel)

    def on_mouse_wheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def populate_weather_items(self, cities_data):
        style = ttk.Style()
        style.configure('cityWeatherItem.TFrame', background="#333333")
        style.configure('removeBgLabel.TLabel', background="#333333", foreground="#FFFFFF")

        frame_cities_weather_column1 = ttk.Frame(self.scrollable_frame, width=600)
        frame_cities_weather_column1.pack(side=tk.LEFT, fill=tk.Y, anchor='nw')

        frame_cities_weather_column2 = ttk.Frame(self.scrollable_frame, width=600)
        frame_cities_weather_column2.pack(side=tk.LEFT, fill=tk.Y, anchor='nw')

        frame_cities_weather_column3 = ttk.Frame(self.scrollable_frame, width=600)
        frame_cities_weather_column3.pack(side=tk.LEFT, fill=tk.Y, anchor='nw')

        for i, city in enumerate(cities_data):
            if i % 3 == 0:
                column = frame_cities_weather_column1
            elif i % 3 == 1:
                column = frame_cities_weather_column2
            else:
                column = frame_cities_weather_column3

            frame_city_weather_item = ttk.Frame(column, padding=10)
            frame_city_weather_item.configure(style='cityWeatherItem.TFrame')
            frame_city_weather_item.pack(side=tk.TOP, anchor='nw', padx=(0, 10), pady=5)

            frame_city_weather_item.bind("<MouseWheel>", self.on_mouse_wheel)

            city_weather_item_label = ttk.Label(frame_city_weather_item, text=city["name"], font=("Roboto", 9), width=17, style="removeBgLabel.TLabel")
            city_weather_item_label.pack(side=tk.TOP, anchor='nw')

            city_weather_item_label.bind("<MouseWheel>", self.on_mouse_wheel)


            city_weather_item_img = ImageTk.PhotoImage(Image.open(city["icon_path"]))
            self.image_references.append(city_weather_item_img)
            city_weather_item_img_label = ttk.Label(frame_city_weather_item, image=city_weather_item_img, style="removeBgLabel.TLabel")
            city_weather_item_img_label.pack(side=tk.TOP, pady=25, fill=tk.X, anchor='nw', expand=False)

            city_weather_item_img_label.bind("<MouseWheel>", self.on_mouse_wheel)

            city_weather_day_night_label = ttk.Label(frame_city_weather_item, text=city["temperature"], font=("Roboto", 9), style="removeBgLabel.TLabel")
            city_weather_day_night_label.pack(side=tk.TOP, anchor='nw')