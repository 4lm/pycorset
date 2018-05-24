import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pycorset.functions import numby
from pycorset.functions import stringy
from pycorset.functions import static

from pycorset import start
