# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-22 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0002_auto_20160322_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dpuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='dpuser',
            name='email',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
