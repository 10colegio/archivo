# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apbase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('nacimiento', models.DateField()),
                ('grado', models.CharField(max_length=2)),
            ],
        ),
    ]