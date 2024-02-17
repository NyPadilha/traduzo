from models.abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: dict):
        super().__init__(data)

    def to_dict(self) -> dict:
        return {
            "name": self.data.get("name"),
            "acronym": self.data.get("acronym"),
        }

    @classmethod
    def list_dicts(cls) -> list:
        return [cls(lan).to_dict() for lan in cls._collection.find()]
