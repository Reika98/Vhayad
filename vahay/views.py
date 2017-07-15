# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Vahay

import json

# Create your views here.

def vahay_details(request, pk):
	if not request.user.is_authenticated:
		return redirect('/')

	return render(request, 'vahay/vahayDetails.html')


def add_vahay(request):
	if not request.user.is_authenticated:
		return redirect('/')

	if request.method == 'POST':
		name = request.POST['name']
		category = request.POST['category']
		contact_details = request.POST['contact_details']
		rent_range = request.POST['rent_range']
		address = request.POST['address']
		description = request.POST['description']
		Vahay.objects.create(owner=request.user, name=name, rent_range=rent_range, category=category,
			contact_details=contact_details, address=address, description=details)
		return redirect('/')

	return render(request, 'vahay/addVahay.html')


def get_list_vahay(request):

	list_vahay = Vahay.objects.all()
	context = {

		'list' : list_vahay

	}
	return HttpResponse(context, content_type="application/json")