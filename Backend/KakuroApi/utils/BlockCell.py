"""
Defines a block on a Kakuro board. Simply exists to set the boundaries of the game area.

Created: 30/01/2025
Author: Aidan Monk
"""

from .CellType import CellType
from .KakuroCell import KakuroCell

class BlockCell(KakuroCell):
    def __init__(self):
        super().__init__(CellType.BLOCK)

    def to_dict(self):
        return {
            "type" : "block"
        }
        
    def __str__(self):
        return f"{self.cell_type.name}"