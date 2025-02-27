import requests
import json

class CurrentWeatherMainLocation:
    def __init__(self, api_key, lat, lon):
        self.api_key = api_key
        self.lat = lat
        self.lon = lon

    def get_weather(self):
        url = "https://api.weather.yandex.ru/graphql/query"
        query = {
            "query": f"""
            {{
                weatherByPoint(request: {{ lat: {self.lat}, lon: {self.lon} }}) {{
                    now {{
                        temperature,
                        condition,
                        humidity,
                        windSpeed,
                        windDirection,
                        pressure
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
                return data['data']['weatherByPoint']['now']
            else:
                print("Error:", response.status_code)
                return None
        except Exception as e:
            print("Exception occurred:", e)
            return None

    def save_weather_to_json(self, filename):
        weather_data = self.get_weather()
        if weather_data:
            with open(filename, 'w', encoding='utf-8') as json_file:
                json.dump(weather_data, json_file, ensure_ascii=False, indent=4)
            print(f"Weather data saved to {filename}")

    def load_weather_from_json(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as json_file:
                return json.load(json_file)
        except Exception as e:
            print("Error loading JSON:", e)
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