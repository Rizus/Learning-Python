import pprint
import requests
from dateutil.parser import parse


class YahooWeatherForecast:

    def __init__(self):
        self._city_cache = {}

    def get(self, city):
        if city in self._city_cache:
            return self._city_cache[city]
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key=DS95BNHZMEBQ9YM2NM7H64YDC&contentType=json"
        print("sending HTTP request...")
        data = requests.get(url).json()
        forecast_data = data["days"]
        forecast = []
        for day_data in forecast_data:
            forecast.append({
                "date": parse(day_data["datetime"]),
                "temp": day_data["tempmax"],
                "uvindex": day_data["uvindex"]
            })
        self._city_cache[city] = forecast
        return forecast


class CityInfo:
    """docstring for CityInfo"""

    def __init__(self, city, weather_forecfst=None):
        self.city = city
        self._wether_forecast = weather_forecfst or YahooWeatherForecast()

    def weather_forecfst(self):
        return self._wether_forecast.get(self.city)


def _main():
    weather_forecfst = YahooWeatherForecast()
    for i in range(5):
        city_info = CityInfo("Odessa", weather_forecfst=weather_forecfst)
    forecast = city_info.weather_forecfst()
    pprint.pprint(forecast)


if __name__ == '__main__':
    _main()
