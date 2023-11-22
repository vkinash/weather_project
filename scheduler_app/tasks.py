from .services.openweathermap import (CityInfo,
                                      CurrentWeatherByCoordinates)
from utils import DBConnect
from models import Weather
from config import get_settings


def task_add_current_temperature_in_city(city_name: str = get_settings().city,
                                         lat: float = get_settings().latitude,
                                         lon: float = get_settings().longitude) -> None:
    if lat and lon:
        latitude = lat
        longitude = lon
    elif city_name != "":
        cur_city = CityInfo(city=city_name)
        coordinates = cur_city.get_coordinates()
        latitude = coordinates["lat"]
        longitude = coordinates["lon"]
    else:
        raise ValueError("Pass 'city_name' or 'lat' and 'lon'")

    weather = CurrentWeatherByCoordinates(lat=latitude, lon=longitude)

    with DBConnect() as db:
        db_weather = Weather(city_name=city_name, temperature=weather.get_temperature())
        db.add(db_weather)
        db.commit()
