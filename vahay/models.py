# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vahay(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	rent = models.IntegerField(default=0)
	category = models.CharField(max_length=100)
	contact_details = models.CharField(max_length=100)
	vote = models.IntegerField(default=0)
	available = models.BooleanField(default=1)
	description = models.CharField(max_length=500)
	address = models.CharField(max_length=500)
	email = models.CharField(max_length=500,default="example@email.com")
	account_num = models.IntegerField(default=0)

	def __str__(self):
		return self.name + " - " + self.owner.username

	def isAvailable(self):
		if self.available == 1:
			return True
		else:
			return False

	def getOwner(self):
		return self.owner.last_name + ", " + self.owner.first_name

	def main_as_json(self):
		return {
			"id" : self.id,
			"name"	: self.name,
			"address": self.address,
			"vote" : self.vote
			}

	def details_as_json(self):
		return {
			"id" : self.id,
			"owner" : self.owner.first_name + " " + self.owner.last_name,
			"name" : self.name,
			"rent": self.rent,
			"category" : self.category,
			"contact_details" : self.contact_details,
			"available" : self.available,
			"description" : self.description,
			"email" : self.email, 	
			"address" : self.address,
			"vote" : self.vote
			}

	def account_as_json(self):
		return {
			"account_num" : self.account_num,
		}	


class Image(models.Model):
	vahay = models.ForeignKey(Vahay, on_delete=models.CASCADE)
	link = models.CharField(max_length=1000)

	def __str__(self):
		return self.vahay.name + " - " + self.link


class Transaction(models.Model):
	sender = models.CharField(max_length=25)
	trans_type = models.CharField(max_length=15)
	recipient = models.CharField(max_length=25)
	remarks = models.CharField(max_length=100)
	time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.id


class Resident(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField(default=0)
	occupation = models.CharField(max_length=100)
	home_address = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	account_num = models.IntegerField(default=0)
	vahay = models.ForeignKey(Vahay, on_delete=models.CASCADE)

	def __str__(self):
		return self.name;

	def account_as_json(self):
		return {
			"account_num" : self.account_num,
		}	
