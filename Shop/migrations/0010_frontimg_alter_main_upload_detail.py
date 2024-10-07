# Generated by Django 5.1.1 on 2024-10-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0009_delete_backimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImgName', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='Front/')),
            ],
        ),
        migrations.AlterField(
            model_name='main_upload',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
