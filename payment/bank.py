import 		http.client
import 		json
import		vahay

from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


conn = http.client.HTTPSConnection("api-uat.unionbankph.com")

def pay(sender,recipient,amount):

	# info = json.loads(request.body)
	# source_account = info['resident_account']
	# amount = info['amount_due']
	vahayy = get_object_or_404(vahay.models.Vahay, pk=recipient)

	result1 = vahay.models.Resident.objects.filter(vahay=vahayy)
	sender = [ obj.account_as_json() for obj in result1 ]
	source_account = sender[0]['account_num']

	result2 = vahay.models.Vahay.objects.filter(pk=recipient)
	recipient = [ obj.account_as_json() for obj in result2 ]
	recipient_account = recipient[0]['account_num']

	amount_pay = str(amount);

	payload = "{\"channel_id\":\"VHAYAD\",\"transaction_id\":\"003\",\"source_account\":"+source_account+",\"source_currency\":\"PHP\",\"target_account\":"+recipient_account+",\"target_currency\":\"PHP\",\"amount\":"+amount_pay+"}"

	headers = {

	    'x-ibm-client-id': "ad4dd380-baf8-4182-8b39-dd27bfee0999",
	    'x-ibm-client-secret': "I6gQ7qE6uN5fM6wV0kT3vA3tY2hB6kR4aI6cD1gV6pX1jS1mT3",
	    'content-type': "application/json",
	    'accept': "application/json"  

	}

	conn.request("POST", "/uhac/sandbox/transfers/initiate", payload, headers)

	res = conn.getresponse()
	data = res.read()

	print(data.decode("utf-8"))

	sample = { 'json': 'waaaaa'}

	return HttpResponse(json.dumps(sample), content_type="application/json")