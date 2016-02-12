# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ponto',
            name='latitude',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='ponto',
            name='longitude',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
    ]
