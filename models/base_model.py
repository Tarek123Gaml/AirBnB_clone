#!/usr/bin/python3
"""
    base_model.py
    - Module
    - Contains parent class BaseModel
"""
import uuid
from datetime import datetime


class BaseModel():
    """
        BaseModel
        - Class object & base class
        - Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
            - BaseModel object instantiation
            - Creates an instance of type 'BaseModel' with params
                - id - unique user id
                - created_at - time instance was created
                - updated_at - time when a change occurs in the instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue  # Skip '__class__'
                if key in ('created_at', 'updated_at'):
                    # Convert string representation to datetime object
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
            Prints class name id & dict in human readable format
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            Public method
            - Updates updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            Public method
            - returns a dictionary containing all keys & values of __dict__
            - includes a new '__class__' key with class name
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
