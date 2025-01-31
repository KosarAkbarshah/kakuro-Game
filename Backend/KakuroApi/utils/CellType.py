"""
Defines the different cells used on a Kakuro board, used in the BlockCell, NumberCell, and SumCell classes to easily identify them.

Created: 30/01/2025
Author: Aidan Monk
"""

from enum import Enum

class CellType(Enum):
    BLOCK = 1
    NUMBER = 2
    SUM = 3
    
