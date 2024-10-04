from django.db import models

# Create your models here.

class Catagory (models.Model):
    name = models.CharField (max_length=30)

    def __str__(self) -> str:
        return self.name

class Main_upload (models.Model):

    title = models.CharField (max_length=20)
    image = models.ImageField (upload_to='photo/')
    detail = models.TextField ()
    price = models.IntegerField ()

    def __str__(self) -> str:
        return self.title