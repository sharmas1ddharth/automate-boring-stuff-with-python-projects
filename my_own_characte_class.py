import re

text = 'RoboCop eats baby food. BABY FOOD.'
ch = re.compile(r'[aeiouAEIOU]')
output = ch.findall(text)
print(output)


# negative character class
text = 'RoboCop eats baby food. BABY FOOD.'
ch = re.compile(r'[^aeiouAEIOU]')
output = ch.findall(text)
print(output)