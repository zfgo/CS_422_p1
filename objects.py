# NAME : accuracy.py
# DATE : 4/20/2023
# DESC : module declaring TimeSeries/Set objects
# AUTHORS : Kareem Taha
from django.db import models

class Set(models.Model):
    def __init__(self) -> None:
        self.name = None
        self.description = None
        self.domain = None
        self.vec_size = None
        self.min_length = None
        self.max_length = None
        self.quantity = None
        self.components = None
        self.contributors = None
        self.paper_ref = None
        self.paper_link = None

class TS(models.Model):
    def __init__(self) -> None:
        self.name = None
        self.description = None
        self.domain = None
        self.units = None
        self.keywords = None
        self.vec_size = None
        self.length = None
        self.period = None
        self.data = None

class TSData:
    def __init__(self) -> None:
        self.date = None
        self.time = None
        self.magnitude = None
        self.features = None