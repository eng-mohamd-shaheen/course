import os
from PIL import Image
import requests
import json
import pandas as pd

""""
url = "https://dukengn.github.io/Dog-facts-API/"

data = requests.get(url)


print(data.status_code)

print(data.request.headers)

print(data.request.body)

print(data.headers["Connection"])
"""

#GET Request
"""""
url_get = 'http://httpbin.org/get'
payload = {"name" : "Joseph" , "ID" : 123}

r=requests.get(url_get,params=payload)

print(r.url)
print(r.request.body)
print(r.status_code)

print(type(r.text))
print(r.headers)

print(r.json()["args"]["ID"])
"""

#POST Request 
"""""
url_post = "http://httpbin.org/post"
payload = {"name" : "Joseph" , "ID" : 123}

r = requests.post(url_post, payload)

print(r.url)

print(r.request.body)
print(r.json()["form"])
"""

#Get Req to Google
"""""
url="http://www.google.com"

r = requests.get(url)

print(r.status_code)

print(r.request.body)

print(r.request.headers)
print(r.headers)#this is the response's headers
"""

#Download an Image
"""""
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

r=requests.get(url)
path=os.path.join(os.getcwd(),'image.png')

# with open(path, 'wb') as f:
#     f.write(r.content)
#Image.open(path)
"""


"""""
#Download a File
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'

r = requests.get(url)
path = os.path.join(os.getcwd(),'my_textfile.txt')

with open(path, 'wb') as f:
    f.write(r.content)

with open(path,'r') as f:
    print(f.read())
"""


""""
url='https://official-joke-api.appspot.com/jokes/ten'

data2 = requests.get(url)

results2 = json.loads(data2.text)

df3 = pd.DataFrame(results2)
df3.drop(columns=["type","id"],inplace=True)
print(df3)
"""

url='https://geocode.xyz/51.50354,-0.12768?geoit=json'

data1=requests.get(url)

print(data1.content)
# res= json.loads(data1.text)
# df=pd.DataFrame(res)
# print(df)









