# Generated by Django 5.1.1 on 2024-10-07 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0010_frontimg_alter_main_upload_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frontimg',
            old_name='image',
            new_name='imageOrg',
        ),
    ]
