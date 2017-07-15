# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vahay(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	rent_range = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	contact_details = models.CharField(max_length=100)
	vote = models.IntegerField(default=0)
	available = models.BooleanField(default=1)
	description = models.CharField(max_length=500)
	address = models.CharField(max_length=500)

	def __str__(self):
		return self.name + " - " + self.owner.username

	def isAvailable(self):
		if self.available == 1:
			return True
		else:
			return False

	def getOwner(self):
		return self.owner.last_name + ", " + self.owner.first_name


class Image(models.Model):
	vahay = models.ForeignKey(Vahay, on_delete=models.CASCADE)
	link = models.CharField(max_length=1000)

	def __str__(self):
		return self.vahay.name + " - " + self.link


class Transaction(models.Model):

	sender 		= models.CharField(max_length=25)
	trans_type 	= models.CharField(max_length=15)
	recipient 	= models.CharField(max_length=25)
	remarks		=  models.CharField(max_length=100)

	def __str__(self):
		return self.id

