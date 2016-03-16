# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=0)),
                ('order', models.IntegerField(null=True)),
            ],
        ),
    ]
