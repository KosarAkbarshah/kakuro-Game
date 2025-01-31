from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from . utils.KakuroBoard import KakuroBoard

# Create your views here.
def home(request):
    board = KakuroBoard()
    return JsonResponse({"board" : board.serialize()})
