# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-18 23:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0006_auto_20180919_0232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='skill',
            new_name='master',
        ),
    ]
