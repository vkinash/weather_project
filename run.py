from fastapi import FastAPI
from fastapi_utils.session import FastAPISessionMaker
from fastapi_utils.tasks import repeat_every
from config import get_settings
from scheduler_app.tasks import task_add_current_temperature_in_city

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Weather project v 1.0"}


@app.on_event("startup")
@repeat_every(seconds=3)  # 1 hour
def task_scheduler() -> None:
    task_add_current_temperature_in_city(city_name=get_settings().city,
                                         lat=get_settings().latitude,
                                         lon=get_settings().longitude)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, debug=True, host="127.0.0.1", port=8000)
