'''This is the main package that contains the DAL, BLL, and View subpackages.'''

__version__ = "1.0.0"

from .DAL import *
from .BLL import *
from .View import *

__all__ = ["DAL", "BLL", "View"]