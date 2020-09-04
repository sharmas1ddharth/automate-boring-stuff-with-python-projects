import re

text = "-----geeks for geeks-----"
split = input()
string = re.compile(f'{split}')
output = string.sub("","-----geeks for geeks-----" )
print(output)