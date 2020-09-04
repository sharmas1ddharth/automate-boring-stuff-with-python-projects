import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('cell: 456-258-2222 work: 555-888-9999')
print(mo)