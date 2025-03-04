from django.urls import path
from . import views

urlpatterns = [
    path('', views.init_board, name="init_board"),
    path('validate/', views.validate_board, name='validate_board')
]