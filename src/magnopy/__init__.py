__version__ = "0.0.0"
__doclink__ = "magnopy.org"
__release_date__ = "undefined"

from . import exceptions, io, magnons, score, spinham
from .exceptions import *
from .io import *
from .magnons import *
from .score import *
from .spinham import *

__all__ = ["__version__", "__doclink__", "__release_date__"]
__all__.extend(spinham.__all__)
__all__.extend(io.__all__)
__all__.extend(magnons.__all__)
__all__.extend(exceptions.__all__)
__all__.extend(score.__all__)
