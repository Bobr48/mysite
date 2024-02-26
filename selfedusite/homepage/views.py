from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

from homepage.models import Car

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'А1', 'content': '''<h1>А1, мелочь</h1> Audi A1 (код кузова — 8X) — субкомпактный автомобиль Audi, представленный широкой общественности 4 марта 2010 года на Женевском автосалоне[1].

Первый Audi на базе VW Polo был создан в 1970-х годах, это был Audi 50 на базе VW Polo I. В 2011 на базе VW Polo V вышел Audi A1[2]. С технической точки зрения Audi А1 создан на базе трёхдверного Volkswagen Polo V, в продажу поступил в сентябре 2010 года. Изначально Audi A1 выпускался в виде трёхдверного хэтчбека. В конце 2011 года появился пятидверный хэтчбэк[3].''',
     'is_published': True},
    {'id': 2, 'title': 'А3', 'content': 'Audi A3 — хэтчбэк малого семейного класса, производимый концерном Audi с 1996 года[1][2]. В 1996—2003 годах выпускалось первое поколение, с 2003 по 2012 — второе, c 2013 по 2020 — третье, а в 2020 появилось 4 поколение (8Y) популярного в Европе компактного автомобиля[3], для российского рынка автомобиль 4-го поколения получил 1.4-литровый турбомотр на 150 сил в паре с 8-диапазонной АКПП и передним приводом[4].', 'is_published': True},
    {'id': 3, 'title': 'А4', 'content': 'Биография А4', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Маленькие'},
    {'id': 2, 'name': 'Средние'},
    {'id': 3, 'name': 'Большие'},
]

def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'homepage/index.html', context=data)


def about(request):
    return render(request, 'homepage/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request, post_id):
    post = get_object_or_404(Car, pk=post_id)
    print(post.content)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected':1
    }
    return render(request, 'homepage/post.html', data)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def show_category(request, cat_id):
    return HttpResponse(f"Отображение статьи с id = {cat_id}")