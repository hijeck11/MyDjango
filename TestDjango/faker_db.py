import django
import os
django.setup()
from django.db import transaction
from faker import Faker
from test_app.models import Magazine, Library, Author, Book, Books, Newspaper

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_app.settings")
fake = Faker()


@transaction.atomic
def generate_fake_data(num_authors, num_libraries, num_books):
    # Создание фейковых библиотек:
    for _ in range(num_libraries):
        name = fake.name()
        city = fake.city()
        Library.objects.create(name=name, city=city)

    # libraries = Library.objects.all()
#
#     # Создание фейковых авторов
#     for _ in range(num_authors):
#         first_name_author = fake.first_name_author()
#         second_name_author = fake.second_name_author()
#         birthday = fake.date_of_birth()
#         Author.objects.create(first_name_author=first_name_author, second_name_author=second_name_author, birthday=birthday)
#
#     authors = Author.objects.all()
#
#     # Создание фейковых книг
#     for _ in range(num_books):
#         title = fake.catch_phrase()
#         author = fake.random_element(authors)
#         library = fake.random_element(libraries)
#         price = fake.pydecimal(min_value=0, max_value=1000, right_digits=2)
#         Book.objects.create(title=title, author=author, library=library, price=price)
#
#     # Создание связей между библиотеками и книгами
#     for library in libraries:
#         books = Book.objects.filter(library=library)
#         library_book = LibraryBook.objects.create(library=library)
#         library_book.books.set(books)
# # Генерация фейковых данных
# generate_fake_data(num_authors=10, num_libraries=5, num_books=50)
generate_fake_data(num_libraries=5)