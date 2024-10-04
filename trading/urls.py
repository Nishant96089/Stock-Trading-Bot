# trading/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('run-bot/', views.run_trading_bot, name='run_trading_bot'),
]
