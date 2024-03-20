#!/usr/bin/python3
"""
    Script that implements the BAseModel class.
"""

from datetime import datetime
import models
import uuid

class BaseModel:
    """
        BaseModel: base class that all the subclasses
        will inherit from.
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        data = self.__dict__.copy()
        data['created_at'] = self.created_at.isoformat()
        data['updateed_at'] = self.updated_at.isoformat()
        data['__class__'] = self.__class__.__name__
        return data

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
