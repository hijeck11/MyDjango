from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Главная</h1>')

def about(request):
    return HttpResponse('<h1>Наш клуб</h1>')

def adress(request):
    return HttpResponse('<h1>На этой страницу указаны адрес и контакты нашего клуба</h1>')

def help(request):
    return HttpResponse('<h1>Помощь</h1>')

def flowers(request):
    return render(request, 'test_app/flowers.html')