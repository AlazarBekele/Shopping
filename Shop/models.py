from django.db import models

# Create your models here.


class News (models.Model):

    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photo/')

    def __str__(self) -> str:
        return self.title