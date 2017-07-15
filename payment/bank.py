import http.client

conn = http.client.HTTPSConnection("api-uat.unionbankph.com")

payload = "{\"channel_id\":\"UHAC_TEAM\",\"transaction_id\":\"001\",\"source_account\":\"XXXXXXXXXX1\",\"source_currency\":\"PHP\",\"target_account\":\"XXXXXXXXXX2\",\"target_currency\":\"PHP\",\"amount\":7}"

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