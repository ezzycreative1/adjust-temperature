from fastapi import FastAPI
from app.api.endpoints import adjust_temperature

app = FastAPI()

app.include_router(adjust_temperature.router)
