from fastapi import APIRouter

import json

default_router = APIRouter()

json_file = "src/data.json"


@default_router.get("/")
async def root():
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data