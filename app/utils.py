"""
    Utilidades de la api
"""
import uvicorn


def begin():
    """Esta funcion le da inicio al servidor"""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
