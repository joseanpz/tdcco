from fastapi import APIRouter
from .model import Solicitud

router = APIRouter()


@router.post("/solicitud")
async def predict(solicitud: Solicitud):
    return {"predict": solicitud.predecir()}
