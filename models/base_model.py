#!/usr/bin/python3
'''module for basemodel'''


import uuid
from datetime import datetime

'''create a basemodel'''


class BaseModel:
    '''A base model class with unbje modification'''

    def __init__(self):
        '''inizialize attribute id and datetime of an instance'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''str function modified'''
        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__))

    def save(self):
        '''save and update time each time we save'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''return dict modified the keywords'''
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
