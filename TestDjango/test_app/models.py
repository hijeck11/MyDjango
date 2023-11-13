from django.db import models

class Testmodel(models.Model):
    firstname_test = models.CharField(max_length=100)
    lastname_test = models.CharField(max_length=100)
    description = models.TextField()
    model_img = models.ImageField(upload_to='img/')


