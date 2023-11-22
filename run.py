import models
import json

from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from scheduler_app.tasks import task_add_current_temperature_in_city
from database import engine
from weather_api.routes import router as weather_router
from fastapi.exceptions import ValidationError
from starlette.responses import JSONResponse


app = FastAPI()
# create database and tables
models.Base.metadata.create_all(bind=engine)
# register route
app.include_router(weather_router)


@app.get("/")
async def index():
    return {"message": "Weather project v 1.0"}


@app.on_event("startup")
@repeat_every(seconds=60*60)  # 1 hour
def task_scheduler() -> None:
    task_add_current_temperature_in_city()


@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    print(f"OMG! The client sent invalid data!: {exc}")
    exc_json = json.loads(exc.json())
    response = {"error": {"message": []}}
    for error in exc_json:
        response["error"]['message'].append(error['loc'][-1]+f": {error['msg']}")
    return JSONResponse(response, status_code=422)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, debug=True, host="127.0.0.1", port=8000)
