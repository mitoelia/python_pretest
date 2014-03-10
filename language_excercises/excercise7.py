import json
import requests

r = requests.get('http://ialpython.apiary.io/people')
emails = json.loads(r.content)

d_out = {}
for email, name in emails.items():
	if name in d_out.keys():
		d_out[name].append(email)
	else:
		d_out[name] = [email]
print d_out

