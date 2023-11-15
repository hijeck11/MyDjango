from django.db import models

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

#todo related_name = 'authors': Это аргумент, который устанавливает
# имя обратного связанного поля для Library. Когда вы используете related_name, Django создает
# обратное поле в модели Library, которое позволяет вам обращаться к связанным авторам через объекты библиотек.


    def __str__(self):
        return self.second_name_author

    def get_books_in_library(self, library):
        return Book.objects.filter(author=self, author__libraries=library)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

#todo models.CASCADE: автоматически удаляет строку из зависимой таблицы, если удаляется связанная строка из главной таблицы

    def __str__(self):
        return self.title