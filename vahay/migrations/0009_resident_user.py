# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 22:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vahay', '0008_auto_20170716_0513'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]