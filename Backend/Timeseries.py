# NAME : Timeseries.py
# DATE : 4/20/2023
# DESC : module defining TimeSeries/Set objects
# AUTHORS : Kareem Taha
#
# Class 1: Set (For sets of multiple TS objects)
# Class 2: TS (For storage of single TS object)
# Class 3: TSData (For storage of DATA within a single TS object)
from django.db import models

class Set(models.Model):
    '''Containers for a single SET of multiple TS objects (defined below), storing set metadata'''
    def __init__(self, name = None, description = None, domain = None, vec_size = None, min_length = None, max_length = None, 
                        quantity = None, components = None, contriutors = None, paper_ref = None, paper_link = None) -> None:
        self.name = name
        self.description = description
        self.domain = domain
        self.vec_size = vec_size
        self.min_length = min_length
        self.max_length = max_length
        self.quantity = quantity
        self.components = components
        self.contributors = contriutors
        self.paper_ref = paper_ref
        self.paper_link = paper_link

class TS(models.Model):
    '''Containers for a single TimeSeries (TS) object, which stores TS data (in the form of a TSData object defined below) & metadata'''
    def __init__(self, name = None, description = None, domain = None, units = None, keywords = None, 
                        vec_size = None, length = None, period = None, data = None) -> None:
        self.name = name
        self.description = description
        self.domain = domain
        self.units = units
        self.keywords = keywords
        self.vec_size = vec_size
        self.length = length
        self.period = period
        self.data = data

class TSData:
    '''Container for the DATA of a single TimeSeries (TS) object, meant for storage in a TS object'''
    def __init__(self, date = None, time = None, magnitude = None, features = None) -> None:
        self.date = None
        self.time = None
        self.magnitude = None
        self.features = None