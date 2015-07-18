#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
r=requests.get('http://api.theysaidso.com/qod.xml')
soup=BeautifulSoup(r.text,'lxml')
print "QUOTE OF THE DAY:"
print soup.body.quote.string
print "-" + soup.body.author.string
input("")
