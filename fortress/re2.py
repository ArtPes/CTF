#!/usr/bin/env python3
import requests
import urllib

with open('messageA', 'rb') as f:
    name=urllib.parse.quote_plus(f.read())

with open('messageB', 'rb') as f:
    password=urllib.parse.quote_plus(f.read())

resp = requests.get(f'http://fortress:7331/t3mple_0f_y0ur_51n5.php?user={name}&pass={password}',
                    headers = {'Host': 'fortress:7331'})
print(resp.text)
