from abc import ABC, abstractmethod
from connect_database.ConnectMySQL import ConnectDatabase
from utils.config import DB_NAME
class BaseControl(ABC):
    def __init__(self,view):
        super().__init__()
        self.view=view
        self.connect=ConnectDatabase(database=DB_NAME)
