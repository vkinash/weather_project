from fastapi import Header, HTTPException
from config import get_settings


async def get_token_header(x_token: str = Header(None)):
    if x_token != get_settings().x_token:
        raise HTTPException(status_code=400, detail="X-Token header invalid")


