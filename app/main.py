from fastapi import FastAPI
from .solicitud import solicitud_router


app = FastAPI()

app.include_router(solicitud_router)