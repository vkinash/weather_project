from pydantic import BaseModel, constr, validator

from datetime import datetime


class WeatherDateSchema(BaseModel):
    date: constr(regex=r'\d{4}-\d{2}-\d{2}')

    @validator('date')
    def validate_date(cls, v: str):
        try:
            v = datetime.strptime(v, '%Y-%m-%d')
            return v
        except ValueError:
            raise ValueError('Incorrect date format, should be YYYY-MM-DD')


class WeatherSchemas(BaseModel):
    weather_time: datetime
    city_name: str
    temperature: float

    class Config:
        orm_mode = True
