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

class Author(models.Model):
    first_name_author = models.CharField(max_length=100)
    second_name_author = models.CharField(max_length=100)
    birthday = models.DateField()
    libraries = models.ManyToManyField(Library, related_name='authors')

    def __str__(self):
        return self.second_name_author

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title