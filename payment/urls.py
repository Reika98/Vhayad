from 	django.conf.urls 	import 	url
from 	. 					import 	bank

urlpatterns = [

	url(r'^pay/', bank.pay),

]