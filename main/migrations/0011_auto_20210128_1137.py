# Generated by Django 3.1.2 on 2021-01-28 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210128_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='src_image',
            new_name='url_image',
        ),
    ]