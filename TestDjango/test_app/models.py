from django.db import models

class Persons(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.DecimalField(max_digits=100)
    address = models.CharField(max_length=100)

# class MyModel(models.Model):
#     field1 = models.CharField(max_length=100)
#     field2 = models.IntegerField()
#     field3 = models.BooleanField(default=False)