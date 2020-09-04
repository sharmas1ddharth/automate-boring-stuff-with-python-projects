import re

text = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 dove, 1 partridge'

xmas = re.compile(r'\d+\s\w+')
output = xmas.findall(text)
print(output)
