# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-03 18:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='name',
        ),
    ]
