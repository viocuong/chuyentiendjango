# Generated by Django 3.1.2 on 2021-01-28 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210127_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='url_image',
            new_name='src_image',
        ),
        migrations.AddField(
            model_name='bill',
            name='image',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
