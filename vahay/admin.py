# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Vahay, Image, Transaction, Resident

# Register your models here.
admin.site.register(Vahay)
admin.site.register(Image)
admin.site.register(Transaction)
admin.site.register(Resident)