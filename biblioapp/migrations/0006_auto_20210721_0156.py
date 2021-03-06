# Generated by Django 3.1.7 on 2021-07-21 01:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioapp', '0005_auto_20210720_2140'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='book',
            name='La Fecha máxima válida es 2021-12-31',
        ),
        migrations.AlterField(
            model_name='book',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='covers'),
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.CheckConstraint(check=models.Q(release_date__lte=datetime.date(2021, 12, 31)), name='La Fecha máxima válida es 2021-12-31'),
        ),
    ]
