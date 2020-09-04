import re
text = 'First Name: Al Last Name: Sweigart'

name = re.compile(r'First Name: (.*) Last Name: (.*)')
a = name.search(text)
print(a.group(1), a.group(2))