# Generated by Django 5.1.1 on 2024-10-14 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0017_secondimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecCardImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardTitle', models.CharField(max_length=20)),
                ('CardImg', models.ImageField(upload_to='SecondCard/')),
            ],
        ),
    ]
