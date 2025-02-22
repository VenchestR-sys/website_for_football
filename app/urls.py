from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='home'),
path('about/', views.about, name='about'),
path('match/', views.match, name='match'),
path('draw/', views.draw, name='draw'),
path('table/', views.table, name='table'),
path('team/', views.team, name='team'),
path('statistic/', views.statistic, name='statistic'),
path('game/', views.game, name='game'),
path('video/', views.video, name='video'),
]