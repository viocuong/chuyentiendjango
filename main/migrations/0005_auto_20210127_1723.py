# Generated by Django 3.1.2 on 2021-01-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210127_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='url_image',
            field=models.CharField(max_length=1000),
        ),
    ]
