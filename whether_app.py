import requests
import json

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather_data(self, city):
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # raises error for 4xx or 5xx

            data = response.json()
            weather_info = {
                "City": f"{data['name']}, {data['sys']['country']}",
                "Temperature": f"{data['main']['temp']}°C",
                "Humidity": f"{data['main']['humidity']}%",
                "Condition": data['weather'][0]['description']
            }
            return weather_info

        except requests.exceptions.HTTPError as e:
            print(f"\n HTTP Error: {e}")
        except requests.exceptions.ConnectionError:
            print("\n Network Error: Please check your internet connection.")
        except requests.exceptions.Timeout:
            print("\n Timeout Error: The request took too long to respond.")
        except KeyError:
            print("\n Unexpected data format received from API.")
        except Exception as e:
            print(f"\n An unexpected error occurred: {e}")
        return None

    def display_weather(self, weather_info):
        print("\n====== Weather Report ======")
        print(f"City: {weather_info['City']}")
        print(f"Temperature: {weather_info['Temperature']}")
        print(f"Humidity: {weather_info['Humidity']}")
        print(f"Condition: {weather_info['Condition']}")
        print("============================")

    def save_to_json(self, weather_info):
        try:
            with open("weather.json", "w") as file:
                json.dump(weather_info, file, indent=4)
            print("\n Data saved successfully to weather.json")
        except Exception as e:
            print(f"\n Failed to save data: {e}")

    def run(self):
        print("=== Simple Weather CLI App ===\n")
        city = input("Enter city name: ").strip()

        weather_info = self.get_weather_data(city)
        if weather_info:
            self.display_weather(weather_info)
            self.save_to_json(weather_info)
        else:
            print("\n Unable to display weather information.")




# --- MAIN EXECUTION ---
def main():
    API_KEY = ""
    app = WeatherApp(API_KEY)
    app.run()

if __name__ == "__main__":
    main()
