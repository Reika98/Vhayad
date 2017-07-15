# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 09:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Vahay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rent_range', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('contact_details', models.CharField(max_length=100)),
                ('vote', models.IntegerField(default=0)),
                ('available', models.BooleanField(default=1)),
                ('description', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='vahay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vahay.Vahay'),
        ),
    ]
