from CellType import CellType
from BlockCell import BlockCell
from NumberCell import NumberCell
from SumCell import SumCell
from KakuroBoard import KakuroBoard

#block cell
cell1 = BlockCell()
#number cell
cell2 = NumberCell(4)
#sum cell
cell3 = SumCell(None, 12)

board = KakuroBoard()

print(board.serialize())
