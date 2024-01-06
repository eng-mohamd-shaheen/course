import requests
#this page has a picture wich we want to download

"""
url = "https://xkcd.com/353/"
r = requests.get(url)
r.encoding='ISO-8859-1'
print(r.encoding)
print(r.content)
print(r.encoding)
# print(dir(r))
# print(help(r))
"""

""""
# #the picture wich we want to download
# url ="https://imgs.xkcd.com/comics/python.png"
# r = requests.get(url)

# print(r.content)
"""

""""
payload = {'page' : 2 , 'count' : 25}

url='https://httpbin.org/get'

r=requests.get(url,params=payload)

print(r.text)
"""

""""
url='https://httpbin.org/post'
payload={'user_name':'Ali' , 'password':'123'}

r=requests.post(url,data=payload)
req_dictionary = r.json();
print(req_dictionary['form'])
"""

""""
url='https://httpbin.org/basic-auth/mohamd/123'

#we use tuples here
r=requests.get(url,auth=('mohamd','123'),timeout=3)

print(r.json()['user'])

"""

url='https://httpbin.org/delay/4'
r=requests.get(url,timeout=3)

print(r)







