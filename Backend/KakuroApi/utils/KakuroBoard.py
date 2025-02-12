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
        self.board = []

    def generate_board(self):
        #generate a random 4x4 for now
        self.board = [
            [BlockCell(), BlockCell(), BlockCell(), SumCell(19, None), SumCell(22, None)],
            [BlockCell(), SumCell(13, None), SumCell(11, 16), NumberCell(7), NumberCell(9)],
            [SumCell(None, 11), NumberCell(1), NumberCell(2), NumberCell(3), NumberCell(5)],
            [SumCell(None, 21), NumberCell(3), NumberCell(1), NumberCell(9), NumberCell(8)],
            [SumCell(None, 17), NumberCell(9), NumberCell(8), BlockCell(), BlockCell()]
        ]
        print(self)

    def set_board(self, board):
        self.board = board
    

    def get_board(self):
        return self.board
    
    def set_number(self, row, column, value):
        if type(self.board[row][column]) == NumberCell:
            self.board[row][column].value = value
        else:
            print("set_number_error - cell is not a number")

    @staticmethod
    def validate_answers(board):
        #check rows
        is_valid = True

        #check horizontally
        for x in range(len(board[0])):
            target_sum = 0
            current_sum = 0 
            count_mode = False

            for y in range(len(board)):
                cell = board[x][y]
                if count_mode:
                    if type(cell) == NumberCell:
                        current_sum += cell.value
                        print("Current sum:", current_sum)
                        if y >= len(board) -1:
                            if current_sum != target_sum:
                                print(f"Validation faileda: {current_sum} ≠ {target_sum} at row {x}, column {y}")
                                is_valid = False
                                count_mode = False
                            else:
                                print("Check passed")
                            current_sum = 0

                    elif type(cell) == BlockCell:
                        if current_sum != target_sum:
                            print(f"Validation failedb: {current_sum} ≠ {target_sum} at row {x}, column {y}")
                            is_valid = False
                        else:
                            print("Check passed")
                            count_mode = False
                        current_sum = 0  

                    elif type(cell) == SumCell:  
                        if current_sum != target_sum:
                            print(f"Validation failedc: {current_sum} ≠ {target_sum} at row {x}, column {y}")
                            is_valid = False
                            count_mode = False
                        current_sum = 0  
                        if cell.right_sum is not None:
                            target_sum = cell.right_sum
                            count_mode = True
                        print("New target sum:", target_sum)

                else:  # count_mode is False
                    if type(cell) == SumCell:
                        if cell.right_sum is not None:
                            print(cell.right_sum)
                            target_sum = cell.right_sum
                            count_mode = True
                            current_sum = 0  # Reset sum for the new count
                            print("New target sum:", target_sum)
            print("-- End of row --")

        #check columns
        for y in range(len(board)):
            target_sum = 0
            current_sum = 0 
            count_mode = False

            for x in range(len(board[0])):
                cell = board[x][y]
                if count_mode:
                    if type(cell) == NumberCell:
                        current_sum += cell.value
                        print("Current sum:", current_sum)
                        if x >= len(board) -1:
                            if current_sum != target_sum:
                                print(f"Validation failedd: {current_sum} ≠ {target_sum} at row {x}, column {y}")
                                is_valid = False
                                count_mode = False
                            else:
                                print("Check passed")
                            current_sum = 0

                    elif type(cell) == BlockCell:
                        if current_sum != target_sum:
                            print(f"Validation failede: {current_sum} ≠ {target_sum} at row {x}, column {y}")
                            is_valid = False
                        else:
                            print("Check passed")
                            count_mode = False
                        current_sum = 0  

                    elif type(cell) == SumCell:  
                        if current_sum != target_sum:
                            print(f"Validation failedf: {current_sum} ≠ {target_sum} at row {x}, column {y}")
                            is_valid = False
                            count_mode = False
                        current_sum = 0  
                        if cell.down_sum is not None:
                            target_sum = cell.down_sum
                            count_mode = True
                        print("New target sum:", target_sum)

                else:  # count_mode is False
                    if type(cell) == SumCell:
                        if cell.down_sum is not None:
                            target_sum = cell.down_sum
                            count_mode = True
                            current_sum = 0  # Reset sum for the new count
                            print("New target sum:", target_sum)
            print("-- End of column --")
        return is_valid

    def serialize(self):
            result = []
            for row in self.board:
                new_row = []
                for cell in row:
                    new_row.append(cell.to_dict())
                result.append(new_row)
            return result
    
    @staticmethod
    def deserialize(board_json):
        deserialized_board = KakuroBoard()
    
        deserialized_board.board = [[None] * len(board_json[0]) for _ in range(len(board_json))]

        for row_index, row_data in enumerate(board_json):
            for col_index, cell_data in enumerate(row_data):
                cell_type = cell_data.get('type')
                print(cell_data)

                if cell_type == 'block':
                    deserialized_board.board[row_index][col_index] = BlockCell()

                elif cell_type == 'sum':
                    right_sum = cell_data.get('right_sum')
                    down_sum = cell_data.get('down_sum')
                    deserialized_board.board[row_index][col_index] = SumCell(down_sum, right_sum)

                elif cell_type == 'number':
                    value = cell_data.get('value')
                    deserialized_board.board[row_index][col_index] = NumberCell(value)
        print(deserialized_board)
        return deserialized_board

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
                    elif cell.down_sum is None:
                        row_str.append(f"{cell.right_sum}/")
                    else:
                        row_str.append(f"{cell.down_sum} / {cell.right_sum}")

                elif isinstance(cell, NumberCell):
                    row_str.append(f"  {cell.value}  ")  # Empty number cell
            board_str += " | ".join(row_str) + "\n"
        return board_str