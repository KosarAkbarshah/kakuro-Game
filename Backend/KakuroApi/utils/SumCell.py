"""
Defines the edge conditions to play the game correctly. down_sum signifies the correct answer for all the NumberCells below the SumCell.
right_sum the correct sum for the NumbeCells to the right of one.
Use 'None' for either of the sum attributes when there is only one direction of sums to check.

Created: 30/01/2025
Author: Aidan Monk
"""

from .KakuroCell import KakuroCell
from .CellType import CellType

class SumCell(KakuroCell):
    def __init__(self, down_sum: int, right_sum: int):
        super().__init__(CellType.SUM)
        self.down_sum = down_sum
        self.right_sum = right_sum

    def to_dict(self):
        return {
            "type" : "sum",
            "down_sum" : self.down_sum,
            "right_sum" : self.right_sum
        }
    
    def __str__(self):
        return f"{self.cell_type.name}, Down Sum: {self.down_sum}, Right Sum: {self.right_sum}"
