# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-17 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=2000)),
                ('image', models.URLField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
