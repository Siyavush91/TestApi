import requests
import json
import random


r = requests.get('https://dog.ceo/api/breed/boxer/images/random')
data = json.loads(r.content)
data1 = json.dumps(data)
print(data1[13:43]) == 'https://images.dog.ceo/breeds/'
