from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.urls import reverse
import os
from datetime import datetime


def format_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = format_current_time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    try:
        workdir = os.getcwd()
        files = os.listdir(workdir)
        file_list = [f for f in files]
        return HttpResponse('\n'.join(file_list))
    except Exception as e:
        return HttpResponse(f'Ошибка: {str(e)}', status=500)

    raise NotImplemented
