# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
	if not request.user.is_authenticated:
		return redirect('/')

	return render(request, 'vhayad/homepage.html')
