# Generated by Django 5.1.1 on 2024-10-12 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0014_uploadcontainer_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadcontainer',
            name='image',
            field=models.ImageField(upload_to='house/'),
        ),
        migrations.AlterField(
            model_name='uploadcontainer',
            name='profileImg',
            field=models.ImageField(upload_to='profile/'),
        ),
    ]
