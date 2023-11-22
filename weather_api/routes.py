import datetime

from fastapi import APIRouter, Depends
from dependencies import get_token_header
from models import Weather
from utils import DBConnect
from config import get_settings
from .schemas import WeatherDateSchema, WeatherSchemas


router = APIRouter(
    prefix="/weather",
    tags=["weather"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/{date}", response_model=list[WeatherSchemas])
async def get_weather(date: str):
    date = WeatherDateSchema(date=date).date
    date_from = date.replace(hour=0, minute=0, second=0, microsecond=0)
    date_to = date.replace(hour=23, minute=59, second=59, microsecond=999999)
    with DBConnect() as db:
        weather = db.query(Weather).filter(Weather.weather_time.between(date_from, date_to),
                                           Weather.city_name == get_settings().city).all()

        return weather

