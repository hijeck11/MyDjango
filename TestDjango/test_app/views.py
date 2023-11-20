from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Testmodel
from .models import Library, Author, Book
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Min, Max, Count
from .forms import BookForm



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

def library_authors(request, library_id):
    library = get_object_or_404(Library, pk=library_id)
    authors = library.get_authors()
    return render(request, 'library_authors.html', {'library': library, 'authors': authors})

def author_books(request, author_id, library_id):
    author = get_object_or_404(Author, pk=author_id)
    library = get_object_or_404(Library, pk=library_id)
    books = author.get_books_in_library(library)
    return render(request, 'author_books.html', {'author': author, 'books': books, 'library': library})

def home(request):
    books = Book.objects.all()
    average_price = Book.objects.aggregate(Avg('price'))['price__avg']
    min_price = Book.objects.aggregate(Min('price'))['price__min']
    max_price = Book.objects.aggregate(Max('price'))['price__max']
    total_books = Book.objects.aggregate(Count('id'))['id__count']

    context = {
        'books': books,
        'average_price': average_price,
        'min_price': min_price,
        'max_price': max_price,
        'total_books': total_books,
    }

    return render(request, 'home.html', context)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('home')