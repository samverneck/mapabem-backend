# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0005_auto_20160209_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ponto',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ponto',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
