# Generated by Django 3.1.7 on 2021-07-22 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioapp', '0008_auto_20210722_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Description',
            new_name='description',
        ),
    ]
