# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-16 05:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_auto_20181016_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='belong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Problem'),
        ),
    ]
