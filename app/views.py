from django.http import HttpResponse
from django.shortcuts import render
from .models import Tabels
 
 
menu = [
    {'title':"Матчи", 'url_name':'match'},
    {'title':"Рисует",'url_name':'draw'},
    {'title':"Таблица",'url_name':'table'},
    {'title':"Видео", 'url_name':'video'},
    {'title':"Азартные игры", 'url_name':'game'},
    {'title':"Cтатистика",'url_name':'statistic'},
    {'title':"Команды",'url_name':'team'},
    {'title':"О нас",'url_name':'about'},
]

def index(request):
    posts=Tabels.published.all()
    tabels =Tabels.published.all() 
    
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': 'posts',
        'cat_selected': 0,
        'tabels':'tabels',
    }
    return render(request, 'index.html', context=data)



def about(request):
    return render(request, 'about.html', {'title': 'О сайте', 'menu': menu})


def table(request):
    tabels = Tabels.objects.filter(is_published=1)
    data = {
        'menu':menu,
        'title': 'Таблица',
        'table': tabels,
    }
    return render(request, 'addpage.html', data)


def video(request):
    return render(request, 'video.html',{'title':'Видео', 'menu':menu})


def draw(request):
     return render(request, 'draw.html',{'title':'Рисует', 'menu':menu})


def game(request):
    return render(request,"game.html",{'title':'Игра', 'menu':menu})


def statistic(request):
     return render(request,"statistic.html",{'title':'Статистика', 'menu':menu})


def team(request):
     return render(request, 'team.html',{'title':'Команда', 'menu':menu})


def match(request):
     return render(request,'match.html',{'title':'Матч', 'menu':menu})