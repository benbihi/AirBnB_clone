#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """A base class for other models"""
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel"""
        self.id = str(uuid.uuid4())
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Return string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance's __dict__"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

