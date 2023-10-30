from django.db import models




class Testmodel(models.Model):
    firstname_test = models.CharField(max_length=100)
    lasttname_test = models.CharField(max_length=100)
    description = models.TextField()


# class MyModel(models.Model):
#     field1 = models.CharField(max_length=100)
#     field2 = models.IntegerField()
#     field3 = models.BooleanField(default=False)