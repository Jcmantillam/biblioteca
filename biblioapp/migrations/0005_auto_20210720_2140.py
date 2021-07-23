# Generated by Django 3.1.7 on 2021-07-20 21:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioapp', '0004_auto_20210720_2137'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='book',
            name='mycustomconstraint_check1',
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.CheckConstraint(check=models.Q(release_date=datetime.date(2021, 12, 31)), name='La Fecha máxima válida es 2021-12-31'),
        ),
    ]
