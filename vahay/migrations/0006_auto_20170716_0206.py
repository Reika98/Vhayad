# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-15 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vahay', '0005_auto_20170716_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='vahay',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vahay.Vahay'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
