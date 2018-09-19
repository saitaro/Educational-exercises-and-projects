# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-19 14:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0002_auto_20180919_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='employer',
        ),
        migrations.RemoveField(
            model_name='master',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='order',
            name='executor',
        ),
        migrations.RemoveField(
            model_name='order',
            name='service',
        ),
        migrations.AddField(
            model_name='master',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='masters', to='CRM.Company'),
        ),
        migrations.AddField(
            model_name='master',
            name='skills',
            field=models.ManyToManyField(related_name='masters', to='CRM.Skill'),
        ),
        migrations.AddField(
            model_name='order',
            name='master',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='CRM.Master'),
        ),
        migrations.AddField(
            model_name='order',
            name='skills',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='CRM.Skill'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=127),
        ),
        migrations.AlterField(
            model_name='master',
            name='name',
            field=models.CharField(max_length=127),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=127),
        ),
    ]
