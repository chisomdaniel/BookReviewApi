#!/usr/bin/env python3
'''The base model for all our database tables'''
from datetime import datetime


class BaseModel:
    
    def serialize(self):
        '''get the string representation of the models'''
        new_dict = self.__dict__.copy()
        
        for key, value in new_dict.items():
            if isinstance(value, datetime):
                new_dict[key] = value.strftime('%Y-%m-%d %H:%M:%S')
        
        if new_dict.get('_sa_instance_state', False):
            del new_dict['_sa_instance_state']
        
        return new_dict

