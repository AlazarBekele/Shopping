from django.db import models

# Create your models here.
class Catagory (models.Model):
    name = models.CharField (max_length=30)

    def __str__(self) -> str:
        return self.name
    
class UploadContainer (models.Model):
    
    title = models.CharField (max_length=40)
    image = models.ImageField (upload_to='house/')
    price = models.CharField (max_length=20)
    length = models.FloatField ()
    bed = models.IntegerField ()
    bath = models.IntegerField ()
    location = models.CharField (max_length=70)
    description = models.TextField (null=True, blank=True)

    profileOwner = models.CharField (max_length=30)
    profileImg = models.ImageField (upload_to='profile/')
    profilePhone = models.IntegerField ()

    def __str__(self) -> str:
        return self.title
    
class SecondImg (models.Model):

    title = models.CharField (max_length=20)
    picture = models.ImageField (upload_to='BackgroundImg')

    def __str__(self) -> str:
        return self.title