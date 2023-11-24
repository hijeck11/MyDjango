from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)


class Testmodel(models.Model):
    firstname_test = models.CharField(max_length=100)
    lastname_test = models.CharField(max_length=100)
    description = models.TextField()
    model_img = models.ImageField(upload_to='img/')

class Library(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_authors(self):
        return Author.objects.filter(libraries=self)

class Author(models.Model):
    first_name_author = models.CharField(max_length=100)
    second_name_author = models.CharField(max_length=100)
    birthday = models.DateField()
    libraries = models.ManyToManyField(Library, related_name='authors')

    def __str__(self):
        return self.second_name_author

    def get_books_in_library(self, library):
        return Book.objects.filter(author=self, author__libraries=library)

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    num_pages = models.PositiveIntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Book(Books):
    volume_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} (Том № {self.volume_number})"


class Magazine(Books):
    issue_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} (Издание № {self.issue_number})"

class Newspaper(Books):
    circulation = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} (Тираж {self.circulation})"

"""related_name = 'authors': Это аргумент, который устанавливает
имя обратного связанного поля для Library. Когда вы используете related_name, Django создает
обратное поле в модели Library, которое позволяет вам обращаться к связанным авторам через объекты библиотек."""

""""models.CASCADE: автоматически удаляет строку из зависимой таблицы, если удаляется связанная строка из главной таблиц"""