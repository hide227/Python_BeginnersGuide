import re

p = re.compile(r'From\s+')
print(p.match('Fromage amk'))

s = 'From amk Thu May 14 19:12:10 1998'
print(p.match(s))

# the re module also provides top-level functions called match(), search(), findall(), sub(), ans so forth.
print(re.match(r'From\s+', 'Fromage amk'))
print(re.match(r'From\s+', s))
