from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Testmodel
from .models import Library, Author, Book
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


def library_list(request):
    libraries = Library.objects.all()
    return render(request, 'library_list.html', {'libraries': libraries})

class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'