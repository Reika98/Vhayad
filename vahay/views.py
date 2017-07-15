# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
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
		name = request.POST.get('name')
		category = request.POST.get('category')
		contact_details = request.POST.get('contact_details')
		rent_range = request.POST.get('rent_range')
		address = request.POST.get('address')
		description = request.POST.get('description')
		Vahay.objects.create(owner=request.user, name=name, category=category, contact_details=contact_details, 
			rent_range=rent_range, vote=1, available=True, description=description, address=address)
		return redirect('/')

	return render(request, 'vahay/addVahay.html')


def get_list_vahay(request):

	list_vahay = Vahay.objects.all()
	context = {

		'list' : list_vahay

	}
	return HttpResponse(context, content_type="application/json")