""" Configuracion inicial de la base de datos """

from motor.motor_tornado import MotorClient
from app.config import config


class MongoInit:
    """Clase que contiene las propiedades basicas de la base de datos."""

    def __init__(self) -> None:
        self.client = MotorClient(config.get("mongo_db_uri"))
        self.database = self.client.products_api
        self.collection = self.database.products


mongo_instance = MongoInit()
