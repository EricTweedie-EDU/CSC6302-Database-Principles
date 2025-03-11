# initialization file for DAL.py
'''This is the DAL package. It contains all the functions that are used
for the Data Access Layer.'''
__version__ = "1.0.0"

from .DAL import *

__all__ = [name for name in dir() if not name.startswith('_')]