import requests
from bs4 import BeautifulSoup as bs
from pyperclip import copy

site = requests.get(input("SITE >"))
blackwords = ",".join(input("BLACKWORDS (comma separated) >"))
blackwords = [each.casefold() for each in blackwords]

site = bs(site.text)

a = site.find_all("div", {"id" :  "work-tags"})
b = [each.find_all("span", {"class" : "styles__children--21o3C"}) for each in a]
c = [each.contents for each in b[0]]
d = sum(c, [])
e = [each for each in d if each.casefold() not in blackwords]
f = ",".join(e)

copy(f)

