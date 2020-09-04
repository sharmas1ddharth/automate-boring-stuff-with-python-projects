import re

text = 'Hy my name is siddharth sharma'

name = re.compile(r'si[\w]+')
out = name.sub("sid",text)
print(out)