import requests
import json
import os

class GetWeatherByHourly:
    def __init__(self, api_key, lat, lon):
        self.api_key = api_key
        self.lat = lat
        self.lon = lon

    def get_hourly_weather(self):
        url = "https://api.weather.yandex.ru/graphql/query"
        query = {
            "query": f"""
            {{
                weatherByPoint(request: {{ lat: {self.lat}, lon: {self.lon} }}) {{
                    forecast {{
                        days(limit: 1) {{
                            hours {{
                                time,
                                temperature,
                                humidity,
                                pressure,
                                windSpeed,
                                windDirection,
                                condition
                            }}
                        }}
                    }}
                }}
            }}
            """
        }

        headers = {
            "Content-Type": "application/json",
            "X-Yandex-Weather-Key": self.api_key
        }

        try:
            response = requests.post(url, json=query, headers=headers)

            print("Response Code:", response.status_code)

            if response.status_code == 200:
                data = response.json()
                print("Response:", data)
                return data['data']['weatherByPoint']['forecast']['days'][0]['hours']
            else:
                print("Error:", response.status_code)
                return None
        except Exception as e:
            print("Exception occurred:", e)
            return None

    def load_weather_from_json(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as json_file:
                try:
                    data = json.load(json_file)
                    formatted_data = []
                    for hour in data:
                        time = hour['time']
                        temperature = hour['temperature']
                        condition = hour['condition']
                        icon = self.get_weather_icon(condition)
                        formatted_data.append((time, temperature, icon))
                    return formatted_data
                except json.JSONDecodeError as e:
                    print("Ошибка при загрузке JSON:", e)
                    return None
        else:
            print("Файл не найден:", filename)
            return None

    def get_weather_icon(self, condition):
        if condition == "OVERCAST" or condition == "CLOUDY":
            return r"./assets/WeatherIconsPack/Clody.png"
        elif condition == "RAIN":
            return r"./assets/WeatherIconsPack/Rain.png"
        elif condition == "SNOW" or condition == "LIGHT_SNOW" or condition == "SLEET":
            return r"./assets/WeatherIconsPack/Snow.png"
        elif condition == "SUNNY" or condition == "CLEAR":
            return r"./assets/WeatherIconsPack/Sunny.png"
        elif condition == "WINDY":
            return r"./assets/WeatherIconsPack/Windy.png"
        elif condition == "FOGGY":
            return r"./assets/WeatherIconsPack/Foggy.png"
        elif condition == "LIGHT_RAIN":
            return r"./assets/WeatherIconsPack/Cloudy_SunnyRain.png"
        elif condition == "HEAVY_RAIN":
            return r"./assets/WeatherIconsPack/CloudyShower.png"
        elif condition == "CLOUDY_SUNNY" or condition == "PARTLY_CLOUDY":
            return r"./assets/WeatherIconsPack/Cloudy_Sunny.png" 
        else:
            return "icon_default.png"


api_key = "b2ea9c54-9867-486a-a3a4-05a1c9656275" 

# Tambov: lat: 52.71833, lon: 41.43333
lat = 52.71833
lon = 41.43333

hourly_weather = GetWeatherByHourly(api_key, lat, lon)

main_location_weather_data = hourly_weather.get_hourly_weather()

# Save the data to a JSON file
if main_location_weather_data:
    with open('./data/hourly_weather_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(main_location_weather_data, json_file, ensure_ascii=False, indent=4)
    print("Hourly weather data saved to hourly_weather_data.json")

    # Optionally, print the data
    for hour in main_location_weather_data:
        time = hour['time']
        temperature = hour['temperature']
        condition = hour['condition']
        icon = hourly_weather.get_weather_icon(condition)

        print(f"Время: {time}, Температура: {temperature}°C, Условие: {condition}, Иконка: {icon}")