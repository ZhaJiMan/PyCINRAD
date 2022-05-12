from . import io
from . import grid
from . import utils
from . import calc
from . import visualize
from . import correct

from .deprecation import Deprecated
from .io import read_level2

__version__ = "1.7.1"

# deprecate `easycalc` namespace
easycalc = Deprecated(
    calc,
    "Please use `calc` instead of `easycalc`.\
The use of namespace `easycalc` is deprecated and will be removed in the future.",
)
