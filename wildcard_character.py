import re

text= 'the cat in the hat sat on the flat mat'

r = re.compile(r'.at')
a = r.findall(text)
print(a)