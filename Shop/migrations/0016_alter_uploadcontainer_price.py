# Generated by Django 5.1.1 on 2024-10-12 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0015_alter_uploadcontainer_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadcontainer',
            name='price',
            field=models.CharField(max_length=20),
        ),
    ]
