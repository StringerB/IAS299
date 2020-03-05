#!/usr/bin/python3

#Author: Jeremy
#Date: Feb2020
#Desc: Scrap some web stuff

#imports here
import urllib3
from bs4 import BeautifulSoup

url = 'http://www.nostarch.com'
headers = {}
#headers['User-Agent'] = 'Googlebot'

#The pool manager will handle threading and connection pooling
req = urllib3.PoolManager()

#make a web request
result = req.request('GET', url)
soup = BeautifulSoup(result.data, 'html.parser')
print(soup)

#Test that it works to this point
#print(result.data)



#eof
