import requests as r

from config import get_settings


class CurrentWeatherByCoordinates:
    def __init__(self, lat: float, lon: float):
        self.lat: float = lat
        self.lon: float = lon
        self.api_key: str = get_settings().api_key
        self.unit: str = "metric"

    def _get_weather_info(self) -> dict:
        response = r.get(f"https://api.openweathermap.org/data/2.5/weather"
                         f"?lat={self.lat}"
                         f"&lon={self.lon}"
                         f"&appid={self.api_key}"
                         f"&units={self.unit}")
        return response.json()

    def get_temperature(self) -> float:
        weather_info = self._get_weather_info()
        return weather_info["main"]["temp"]


class CityInfo:
    def __init__(self, city: str):
        self.city: str = city
        self.api_key: str = get_settings().api_key

    def _get_city_info(self) -> list:
        response = r.get(f"http://api.openweathermap.org/geo/1.0/direct?q={self.city}&limit=5&appid={self.api_key}")
        if not response.json():
            raise ValueError({"error": "Something with openweathermap API response. Not data found"})
        return response.json()

    def get_coordinates(self) -> dict:
        city_info = self._get_city_info()
        lat = city_info[0].get("lat", None)
        lon = city_info[0].get("lon", None)
        if not lat or not lon:
            raise ValueError({"error": "latitude or longitude or both are empty"})
        return {"lat": lat, "lon": lon}

