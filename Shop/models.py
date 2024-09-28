from django.db import models

# Create your models here.


class HeaderImg (models.Model):

    image = models.ImageField(upload_to='photo/')
