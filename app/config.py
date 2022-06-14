""" Modulo que inicializa la configuracion de la API"""
import os
from dotenv import load_dotenv

load_dotenv()

config = {"mongo_db_uri": os.environ["MONGO_DB_URI"]}
