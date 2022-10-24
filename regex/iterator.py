import re

p = re.compile(r'\d+')
iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
print(iterator)

for match in iterator:
    print(match.span())
