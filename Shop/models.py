from django.db import models

# Create your models here.

class Catagory (models.Model):
    name = models.CharField (max_length=30)

    def __str__(self) -> str:
        return self.name

class Main_upload (models.Model):

    title = models.CharField (max_length=20)
    image = models.ImageField (upload_to='photo/')
    detail = models.TextField (null=True, blank=True)
    price = models.IntegerField ()
    catagory = models.ForeignKey(Catagory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
class FrontImg (models.Model):

    ImgName = models.CharField (max_length=25)
    image = models.ImageField (upload_to='Front/')

    def __str__(self) -> str:
        return self.ImgName