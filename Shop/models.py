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
    catagory = models.ForeignKey(Catagory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
class BackImg (models.Model):

    title = models.CharField (max_length=20)
    picture = models.ImageField (upload_to='Back/')

    def __str__(self) -> str:
        return self.title