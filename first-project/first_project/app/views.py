import os

from django.http import HttpResponse
from django.shortcuts import render, reverse

import datetime


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
def home_view(request):
 def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = None
    delta = datetime.timedelta(hours=3, minutes=0)
    current_time = (datetime.datetime.now()+delta).time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    template_name = 'app/workdir.html'
    path = '.'
    file_list = os.listdir(path)
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    raise NotImplemented
    context = {
        'files': file_list
    }
    return render(request, template_name, context)
    # raise NotImplemented