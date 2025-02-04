"""
Defines a cell representing an area the player can enter a number into. Use 0 when the user has not entered anything yet.
Sum these together to check for correct answers.

Created: 30/01/2025
Author: Aidan Monk
"""

from .KakuroCell import KakuroCell
from .CellType import CellType

class NumberCell(KakuroCell):
    def __init__(self, value: int):
        super().__init__(CellType.NUMBER)
        self.value = value

    def to_dict(self):
        return {
            "type" : "number",
            "value" : self.value
        }

    def __str__(self):
        return f"{self.cell_type.name}, Value: {self.value}"