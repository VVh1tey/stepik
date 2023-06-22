import requests
import re

all_links = []

A_link, B_link = input(), input()
A_links = re.findall("href=\"\'[\"\']", requests.get(A_link).text)

for link in A_links:
  html = requests.get(link.replace('stepic.org', 'stepik.org')).text
  c_links = re.findall("href=\"\'[\"\']", html)
  if c_links != None or c_links != []:
    c_links = list(
      map(lambda x: x.replace('stepic.org', 'stepik.org'), c_links))
    all_links.extend(c_links)

if B_link in all_links:
  print("Yes")
else:
  print("No")
