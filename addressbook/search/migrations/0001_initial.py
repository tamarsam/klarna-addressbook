# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 11:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('avatar_image', models.CharField(max_length=200)),
                ('avatar_origin', models.URLField()),
                ('email', models.EmailField(max_length=200)),
                ('quote', models.CharField(max_length=500)),
                ('chuck', models.CharField(max_length=500)),
                ('birthday', models.DateField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='search.Address')),
            ],
        ),
    ]