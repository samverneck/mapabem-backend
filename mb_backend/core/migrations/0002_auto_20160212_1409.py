# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 16:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='localizacao',
            old_name='pontoElemento',
            new_name='localizacaoElemento',
        ),
    ]