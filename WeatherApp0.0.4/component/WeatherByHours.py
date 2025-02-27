import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime

class WeatherByHour(tk.Frame):
    def __init__(self, parent, style, weather_data, left_arrow_img_path, right_arrow_img_path):
        super().__init__(parent)
        
        self.style = style
        self.weather_data = weather_data
        
        self.left_arrow_img = ImageTk.PhotoImage(Image.open(left_arrow_img_path))
        self.left_arrow_btn = ttk.Button(self, text="Left", image=self.left_arrow_img, takefocus=False, command=self.scroll_left)
        self.left_arrow_btn.pack(side=tk.LEFT, fill=tk.Y, padx=5)

        self.right_arrow_img = ImageTk.PhotoImage(Image.open(right_arrow_img_path))
        self.right_arrow_btn = ttk.Button(self, text="Right", image=self.right_arrow_img, takefocus=False, command=self.scroll_right)
        self.right_arrow_btn.pack(side=tk.RIGHT, fill=tk.Y, padx=5, anchor='nw')

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH)

        self.my_canvas = tk.Canvas(self.main_frame, width=460, height=170)
        self.my_canvas.pack(side=tk.TOP, fill=tk.BOTH)

        self.second_frame = tk.Frame(self.my_canvas)

        self.weather_icons = []
        self.style.configure('HourCard.TFrame', background="#333333")
        self.style.configure('HourCard.TLabel', background="#333333", foreground="#FFFFFF")

        self.populate_weather_data()

        self.my_canvas.create_window((0, 0), window=self.second_frame)

        self.main_frame.bind("<Configure>", self.update_scrollregion)
        self.my_canvas.bind("<MouseWheel>", self.on_mouse_wheel) 

        self.second_frame.bind("<MouseWheel>", self.on_mouse_wheel)

    def populate_weather_data(self):
        for hour, temperature, icon_path in self.weather_data:

            time_str = hour
            time_obj = datetime.fromisoformat(time_str) 
            formatted_time = time_obj.strftime("%H:%M")

            original_image = Image.open(icon_path)
            
            resized_image = original_image.resize((50, 50))

            weather_icon = ImageTk.PhotoImage(resized_image)
            self.weather_icons.append(weather_icon) 

            frame_by_hour_card_item = ttk.Frame(self.second_frame, padding=10, cursor="hand2")
            column_index = len(self.weather_icons) - 1 
            frame_by_hour_card_item.grid(row=0, column=column_index, padx=5, pady=5)
            frame_by_hour_card_item.configure(style='HourCard.TFrame')

            frame_by_hour_card_item.bind("<MouseWheel>", self.on_mouse_wheel)

            bhci_hour_label = ttk.Label(frame_by_hour_card_item, text=formatted_time, font=("Roboto", 9), style='HourCard.TLabel')
            bhci_hour_label.pack(side=tk.TOP, expand=True)

            bhci_hour_label.bind("<MouseWheel>", self.on_mouse_wheel)

            bhci_hour_weather_ic_label = ttk.Label(frame_by_hour_card_item, image=weather_icon, style='HourCard.TLabel')
            bhci_hour_weather_ic_label.pack(side=tk.TOP, fill=tk.NONE, pady=10, anchor='center', expand=True)

            bhci_hour_weather_ic_label.bind("<MouseWheel>", self.on_mouse_wheel)

            bhci_hour_weather_temperature_label = ttk.Label(frame_by_hour_card_item, text=temperature, font=("Roboto", 12, "bold"), style='HourCard.TLabel')
            bhci_hour_weather_temperature_label.pack(side=tk.TOP, fill=tk.NONE, pady=10, anchor='center', expand=True)

            bhci_hour_weather_temperature_label.bind("<MouseWheel>", self.on_mouse_wheel)

    def update_scrollregion(self, event):
        self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all"))

    def on_mouse_wheel(self, event):
        self.my_canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")

    def scroll_left(self):
        self.my_canvas.xview_scroll(-3, "units")

    def scroll_right(self):
        self.my_canvas.xview_scroll(3, "units")