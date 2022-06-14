"""
    Punto de entrada para la API de productos
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.utils import begin
from app.core.db import mongo_instance

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    """Se ejecuta al iniciar el servicio"""
    print("Servicio inicializado...")


@app.on_event("shutdown")
async def shutdown_event():
    """Se ejecuta al cerrar el servicio"""
    mongo_instance.close()
    print("Servicio finalizado...")


@app.get("/")
def root():
    """Punto de entrada de la API"""
    return JSONResponse(
        content={
            "msg": "hello world",
        },
        status_code=200,
        media_type="application/json",
    )


if __name__ == "__main__":
    begin()
