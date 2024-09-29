from django.db import models

# Create your models here.


class HeaderImg (models.Model):

    image = models.ImageField(upload_to='photo/')

class News (models.Model):

    title = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.title