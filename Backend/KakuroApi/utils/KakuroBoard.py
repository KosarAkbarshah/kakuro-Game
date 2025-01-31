"""
Represents a single game board of Kakuro

Created: 30/01/2025
Author: Aidan Monk
"""

from .NumberCell import NumberCell
from .SumCell import SumCell
from .BlockCell import BlockCell
from .CellType import CellType

class KakuroBoard:
    def __init__(self):
        #just make a random 4x4 for now
        self.board = [
            [BlockCell(), BlockCell(), BlockCell(), SumCell(19, None), SumCell(22, None)],
            [BlockCell(), SumCell(13, None), SumCell(11, 16), NumberCell(0), NumberCell(0)],
            [SumCell(None, 11), NumberCell(0), NumberCell(0), NumberCell(0), NumberCell(0)],
            [SumCell(None, 21), NumberCell(0), NumberCell(0), NumberCell(0), NumberCell(0)],
            [SumCell(None, 17), NumberCell(0), NumberCell(0), BlockCell(), BlockCell()]
        ]

    def serialize(self):
            result = []
            for row in self.board:
                new_row = []
                for cell in row:
                    new_row.append(cell.to_dict())
                result.append(new_row)
            return result
    

    def __str__(self):
        board_str = ""
        for row in self.board:
            row_str = []
            for cell in row:
                if isinstance(cell, BlockCell):
                    row_str.append(" ██ ")  # Blocked cells as solid squares
                elif isinstance(cell, SumCell):
                    if cell.right_sum is None:
                        row_str.append(f"/{cell.down_sum}")
                    else:
                        row_str.append(f"{cell.right_sum}/")

                elif isinstance(cell, NumberCell):
                    row_str.append("    ")  # Empty number cell
            board_str += " | ".join(row_str) + "\n"
        return board_str