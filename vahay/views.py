# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vahay
from django.core import serializers
import json

# Create your views here.

def vahay_details(request, pk):
	if not request.user.is_authenticated:
		return redirect('/')

	vahay = get_object_or_404(Vahay, pk=pk)
	context = {
		'vahay': vahay
	}
	return render(request, 'vahay/vahayDetails.html', context=context)


def add_vahay(request):
	if not request.user.is_authenticated:
		return redirect('/')

	if request.method == 'POST':
		name = request.POST.get('name')
		category = request.POST.get('category')
		contact_details = request.POST.get('contact_details')
		rent= request.POST.get('rent')
		address = request.POST.get('address')
		description = request.POST.get('description')
		email = request.POST.get('email')
		accountnum = request.POST.get('accountnum')
		Vahay.objects.create(owner=request.user, name=name, category=category, contact_details=contact_details, 
			rent=rent, vote=1, available=True, description=description, address=address, email=email,
			account_num=accountnum)
		return redirect('/')

	return render(request, 'vahay/addVahay.html')


def edit_vahay(request, pk):
	if not request.user.is_authenticated:
		return redirect('/')

	vahay = get_object_or_404(Vahay, pk=pk)
	context = {
		'vahay': vahay
	}

	if request.method == "POST":
		vahay.name = request.POST.get('vahay_name')
		vahay.rent = request.POST.get('rent')
		vahay.category = request.POST.get('category')
		vahay.contact_details = request.POST.get('contacts')
		vahay.address = request.POST.get('address')
		vahay.description = request.POST.get('description')
		vahay.email = request.POST.get('email')
		vahay.account_num = request.POST.get('accountnum')
		if request.POST.get('available', None) == None:
			vahay.available = 0
		else:
			vahay.available = 1

		vahay.save()
		if request.POST['image_link']:
			image_link = request.POST.get('image_link')
			Image.objects.create(vahay=vahay, link=image_link)
		return redirect('/')

	return render(request, 'vahay/editVahay.html', context=context)


def delete_vahay(request, pk):
	vahay = get_object_or_404(Vahay, pk=pk)
	vahay.delete()

	return redirect('/')

def get_list_vahay(request):

	# list_vahay = serializers.serialize('json', Vahay.objects.all())
	list_obj = Vahay.objects.all()
	# vahays = [obj.as_json() for obj in list_obj]
	
	print "GET list_vahay"
	# return HttpResponse(list_vahay, content_type="application/json")
	list_vahay = [ obj.main_as_json() for obj in list_obj ]
	return HttpResponse(json.dumps({"houses": list_vahay}), content_type='application/json')



def m_get_vahay(request, pk):

	# list_vahay = serializers.serialize('json', Vahay.objects.all())
	list_obj = Vahay.objects.filter(pk=pk)
	# vahays = [obj.as_json() for obj in list_obj]
	
	print "GET vahay"
	# return HttpResponse(list_vahay, content_type="application/json")
	vahay = [ obj.details_as_json() for obj in list_obj ]
	return HttpResponse(json.dumps({"houses": vahay}), content_type='application/json')