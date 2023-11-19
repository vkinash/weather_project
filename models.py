from sqlalchemy import Column, Integer, String, DateTime, Float, Index
from database import Base
from config import get_settings

import datetime


class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True)
    city_name = Column(String)
    temperature = Column(Float)
    weather_time = Column(DateTime, default=datetime.datetime.now()) # .strftime("%Y-%m-%d")
    __table_args__ = (Index("ind_city_date", city_name, weather_time),)
