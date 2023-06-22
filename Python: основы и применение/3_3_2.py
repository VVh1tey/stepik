import re
import requests

rq = requests.get(input().strip())
pattern = r'\<a[^>]*\bhref[\s]?\=\s?(?:\'|\")?(?:\w+\:\/\/)?(\w[\w\.\-]*)'

links = re.findall(pattern, rq.text)

for domain in sorted(set(links)):
  print(domain)