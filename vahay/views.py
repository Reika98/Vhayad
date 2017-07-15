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


def get_list_vahay(request):

	list_vahay = Vahay.objects.all()
	context = {

		'list' : list_vahay

	}
	return HttpResponse(context, content_type="application/json")