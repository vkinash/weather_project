from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Weather project v 1.0"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, debug=True, host="127.0.0.1", port=8000)
