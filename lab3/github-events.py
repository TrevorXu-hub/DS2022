#!/usr/bin/env python3


import os
import json
import requests
GHUSER = os.getenv('TrevorXu_hub')
url = 'https://api.github.com/users/{}/events'.format(GHUSER)
r = json.loads(requests.get(url).text)

for x in r[:5]:
  event = x['type'] + ' :: ' + x['repo']['name']
  print(event)
