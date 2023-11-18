import datetime

from .services.openweathermap import (CityInfo,
                                      CurrentWeatherByCoordinates)


def task_add_current_temperature_in_city(city_name: str = None, lat: float = None, lon: float = None) -> dict:
    if city_name != "":
        cur_city = CityInfo(city=city_name)
        coordinates = cur_city.get_coordinates()
        latitude = coordinates["lat"]
        longitude = coordinates["lon"]
    elif lat and lon:
        latitude = lat
        longitude = lon
    else:
        raise ValueError("Pass 'city_name' or 'lat' and 'lon'")

    weather = CurrentWeatherByCoordinates(lat=latitude, lon=longitude)
    tem, time = weather.get_temperature(), datetime.datetime.now()
    print(weather.get_temperature(), datetime.datetime.now())
