# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-15 21:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vahay', '0008_auto_20170716_0513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vahay.Resident')),
                ('vahay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vahay.Vahay')),
            ],
        ),
    ]
