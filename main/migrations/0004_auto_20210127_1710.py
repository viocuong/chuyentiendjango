# Generated by Django 3.1.2 on 2021-01-27 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210123_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='file_name',
            new_name='url_image',
        ),
    ]