from pydantic import BaseModel


class WeatherBaseSchema(BaseModel):
    weather_time: str


class WeatherSchemas(WeatherBaseSchema):
    city_name: str
    temperature: float

    class Config:
        orm_mode = True
