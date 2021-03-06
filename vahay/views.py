# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vahay, Resident, Transaction
from .models import Image, Payment, Reservation
from django.core import serializers


import payment
import json

# Create your views here.

def vahay_details(request, pk):
	if not request.user.is_authenticated:
		return redirect('/')

	vahay = get_object_or_404(Vahay, pk=pk)
	images = Image.objects.filter(vahay=vahay)
	residents = Resident.objects.filter(vahay=vahay)
	context = {
		'vahay': vahay,
		'images': images,
		'residents': residents
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


def delete_resident(request, pk):
	resident = get_object_or_404(Resident, pk=pk)
	resident.delete()

	return redirect('/')


def resident_profile(request, pk):
	resident = get_object_or_404(Resident, pk=pk)
	payment = get_object_or_404(Payment, resident=resident)
	print resident.name
	context = {
		'resident': resident,
		'payment': payment
	}

	return render(request, 'vahay/residentProfile.html', context=context)
	

def reservations(request, pk):
	if not request.user.is_authenticated:
		return redirect('/')

	vahay = get_object_or_404(Vahay, pk=pk)
	transactions = Reservation.objects.filter(recipient=vahay)
	context = {
		'transactions': transactions,
		'vahay' : vahay
	}

	return render(request, 'vahay/reservations.html', context=context)


def confirm_reservation(request, pk):
	if not request.user.is_authenticated:
		return redirect('/')

	transaction = get_object_or_404(Reservation, pk=pk)
	vahay = transaction.recipient
	sender = transaction.sender
	sender.vahay = vahay
	sender.save()

	transaction.delete()
	Payment.objects.create(vahay=vahay,resident=sender, amount=vahay.rent)

	images = Image.objects.filter(vahay=vahay)
	residents = Resident.objects.filter(vahay=vahay)
	context = {
		'vahay': vahay,
		'images': images,
		'residents': residents
	}

	return render(request, 'vahay/vahayDetails.html', context=context)


def approve_reservation(request, pk):

	if not request.user.is_authenticated:
		return redirect('/')

	transaction = get_object_or_404(Transaction, pk=pk)
	if request.method == 'POST':
		transaction.trans_type = 'approved'
		transaction.save()
		response = payment.bank.pay(transaction.recipient,transaction.sender)

		resident = get_object_or_404(Vahay, pk=transaction.sender)
		resident.vahay = transaction.recipient
		resident.save()

	return redirect('/')

def deny_reservation(request, pk):

	if not request.user.is_authenticated:
		return redirect('/')

	transaction = get_object_or_404(Transaction, pk=pk)
	if request.method == 'POST':
		transaction.trans_type = 'denied'
		transaction.save()

	return redirect('/')


#MOBILE
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


def reserve_vahay(request, email, vahayId):

	sender_name = email
	print sender_name

	result = Resident.objects.filter(email=sender_name)
	sender = [ obj.account_as_json() for obj in result ]
	sender_id = sender[0]['id']

	resident = get_object_or_404(Resident, pk=sender_id)

	recipient = get_object_or_404(Vahay, pk=vahayId)
	# result1 = vahay.models.Vahay.objects.filter(owner=recipient)
	# recipient = [ obj.account_as_json() for obj in result ]
	# recipient_id = recipient[0]['account_num']

	remarks = ''

	print "POST reservation"
	new_transaction = Reservation.objects.create(sender=resident,recipient=recipient,remarks=remarks)
	return HttpResponse(json.dumps({'success':'yehey'}), content_type='application/json')


def pay_rental(request, email):
	print "POST payment"
	sender_name = email

	result = Resident.objects.filter(email=sender_name)
	sender = [ obj.account_as_json() for obj in result ]
	sender_id = sender[0]['id']

	vahay = sender[0]['vahay']
	recipient = vahay.id
	trans_type = 'payment'
	remarks = ''
	print "POST payment"
	new_transaction = Transaction.objects.create(sender=sender_id,recipient=recipient,trans_type=trans_type,remarks=remarks)
	trans_id = new_transaction.id

	print "POST payment"
	response = payment.bank.pay(sender_id,recipient,vahay.rent,trans_id)


	resident = get_object_or_404(Resident, pk=sender_id)
	payments = get_object_or_404(Payment, resident=resident)

	amount_to_pay = payments.amount
	payments.amount = 0
	payments.save();
	print payments.amount
	return HttpResponse(json.dumps({'success':'yehey', 'balance': amount_to_pay}), content_type='application/json')


def cancel_reservation(request, pk):

	transaction = get_object_or_404(Transaction, pk=pk)
	if request.method == 'POST':
		transaction.trans_type = 'cancelled'
		transaction.save()
		print "GET cancel reservation"
		return HttpResponse(json.dumps({'success':'cancelled'}), content_type='application/json')


def get_balance(request, email):

	result = Resident.objects.filter(email=email)
	resident = [ obj.account_as_json() for obj in result ]
	resident_id = resident[0]['id']

	payment = get_object_or_404(Payment, pk=resident_id)
	balance = payment.amount

	return HttpResponse(json.dumps({'balance': balance}), content_type='application/json')