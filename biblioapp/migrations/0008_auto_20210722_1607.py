# Generated by Django 3.1.7 on 2021-07-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioapp', '0007_auto_20210722_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='subtitle',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='editor',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
