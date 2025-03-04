from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from . utils.KakuroBoard import KakuroBoard

#create/reset the board, just use a premade 4x4 for now
@api_view(['GET'])
def init_board(request):
    board = KakuroBoard()  # Create a new board instance
    board.generate_board()
    return JsonResponse({"board": board.serialize()})

@api_view(['POST'])
def validate_board(request):
    kakuro_board = KakuroBoard.deserialize(request.data.get('board'))
    is_valid = KakuroBoard.validate_answers(kakuro_board.board)

    return JsonResponse({
        "is_valid": is_valid  # Send the validity status back
    })


