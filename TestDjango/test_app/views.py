from django.shortcuts import render
from django.http import HttpResponse
from .models import Testmodel
from django.shortcuts import render, get_object_or_404



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

def index(request):
    num_img = Testmodel.objects.all()
    return render(request, 'test_app/index.html', context={'num_img': num_img})

def image_detail(request, image_id):
    image = get_object_or_404(Testmodel, pk=image_id)
    return render(request, 'test_app/image_detail.html', {'image': image})