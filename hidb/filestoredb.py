from typing import Dict
from datetime import datetime

from .db import DB
from .wrapper import fileWrapper, dataWrapper


class fileStoreDB(DB):
    def __init__(self, location="./"):
        super().__init__()
        self.filestore = fileWrapper()
        self.location = location

    def addNewData(self, key: str, value: Dict, ttl: int):
        self.filestore.keys.add(key)
        self.filestore.data[key] = dataWrapper(value, ttl)

    def showData(self, key: str):
        currtime = datetime.now().time()
        datatime = self.filestore.data[key].timestamp
        return self.filestore.data[key].data

    def saveData(self):
        pass

    def create(self, key: str, value: Dict, ttl: int = None):
        if len(key) > 32:
            raise KeyError(f"Length of key: {len(key)} exceeds limits should be: 32")
        if key in self.filestore.keys:
            raise KeyError(f"{key} does not exist")
        self.addNewData(key, value, ttl)
        self.saveData()

    def read(self, key: str):
        if len(key) > 32:
            raise KeyError(f"Length of key: {len(key)} exceeds limits should be: 32")
        if key not in self.filestore.keys:
            raise KeyError(f"{key} does not exist")

        return self.showData(key)

    def delete(self, key: str):
        if len(key) > 32:
            raise KeyError(f"Length of key: {len(key)} exceeds limits should be: 32")
        if key not in self.filestore.keys:
            raise KeyError(f"{key} does not exist")
        self.filestore.keys.remove(key)
        del self.filestore.data[key]
        self.saveData()
