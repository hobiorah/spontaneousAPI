# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-03 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0004_favorites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visited',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeid', models.CharField(max_length=50)),
                ('visit_date', models.DateField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myproject.DPUser')),
            ],
        ),
        migrations.RenameModel(
            old_name='Favorites',
            new_name='Favorite',
        ),
    ]
