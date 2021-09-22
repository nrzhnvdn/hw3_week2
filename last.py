#19
# # import os
# # for root, dirs, files in os.walk("."):  
# #     for filename in files:
# #         print(filename)
# # заходим в webhook.site и вставим через edit. 
# # потом https://jsonformatter.curiousconcept.com/# заходим, чтобы посмотреть в нормальном виде

import json
import requests

url = 'https://webhook.site/9dd2b9c8-6cc3-4616-b459-2f6f68cbf29b'
x = requests.get(url)

data = x.json()
for i in data:
      if i['eyeColor'] == "green":
        print(i['name']['first'])
     
total_balance = 0

for i in data:
  if i["eyeColor"] == "green":
    total_balance += float(i["balance"][1:2] + i["balance"][3:])

print(round(total_balance))

#20
#!/usr/bin/python
# -*- coding: utf-8 -*-
# body.encode('utf-8')
import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
text = input('Type a word: ')
payload = "source=en&target=ru&q=" + text
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': "703ebbf692msh1fdc19dde6eda73p12b23bjsndae33a4088fd"
    }

response = requests.request("POST", url, data=payload, headers=headers)

text = response.json()

print(text)









