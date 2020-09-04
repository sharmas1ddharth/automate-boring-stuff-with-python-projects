import re

text = 'helloshdjshdhjsd word'
caret = re.compile(r'^hello')
a = caret.search(text)
print(a)

t = 'your number is 554'

num = re.compile(r'\d$')
s = num.search(t)
print(s)