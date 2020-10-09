import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class SingletonMeta(type):

    _instances = {}

    def __call__(cls):
        if cls not in cls._instances:
            instance = super().__call__()
            cls._instances[cls] = instance
        return cls._instances[cls]

class Connection(metaclass=SingletonMeta):
    _db = None


    def __init__(self):
        if self._db == None:
            self._db = psycopg2.connect(host = os.environ["host"],
            database = os.environ["database"],
            user = os.environ["db_user"],
            password = os.environ["db_passwd"])


