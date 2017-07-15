import 		http.client
import 		json
import		vahay

from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User


conn = http.client.HTTPSConnection("api-uat.unionbankph.com")

def pay(request):

	# info = json.loads(request.body)
	# source_account = info['resident_account']
	# amount = info['amount_due']

	query = vahay.models.Vahay.objects.filter(name='rafelle')
	recipient = [ obj.main_as_json() for obj in list_obj ]
	print recipient['account_num']

	# payload = "{\"channel_id\":\"VHAYAD\",\"transaction_id\":\"003\",\"source_account\":\"101828352677\",\"source_currency\":\"PHP\",\"target_account\":\"101366553205\",\"target_currency\":\"PHP\",\"amount\":10}"

	# headers = {

	#     'x-ibm-client-id': "ad4dd380-baf8-4182-8b39-dd27bfee0999",
	#     'x-ibm-client-secret': "I6gQ7qE6uN5fM6wV0kT3vA3tY2hB6kR4aI6cD1gV6pX1jS1mT3",
	#     'content-type': "application/json",
	#     'accept': "application/json"  

	# }

	# conn.request("POST", "/uhac/sandbox/transfers/initiate", payload, headers)

	# res = conn.getresponse()
	# data = res.read()

	# print(data.decode("utf-8"))

	sample = { 'json': 'waaaaa'}

	return HttpResponse(json.dumps(sample), content_type="application/json")