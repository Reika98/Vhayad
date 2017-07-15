# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
	context = {}

	if request.user.is_authenticated:
		return render(request, 'vhayad/homepage.html', context=context)

	if request.method == 'POST':
		username = request.POST['username']
		password =  request.POST['password']
		user = authenticate(username=username, password=password)

		if user:
			print "dir"
			login(request, user)
			return render(request, 'vhayad/homepage.html', context=context)

		else:
			print	"or dir"
			context['error_message'] = 'Invalid username or password'
			context['username'] = username

	return render(request, 'vhayad/signin.html', context=context)
