#! python3

# Phone and Email Extractor - This program finds phone number and email from the clipboard

import re, pyperclip

text = str(pyperclip.paste())    #+91 7830205284 and email is ssiddharth408@gmail.com

# Phone number regex
phone_number = re.compile(r'''((\+\d+)                # Country code
                          (\s|-|\.)?                  # Separator
                          (\d{10}))''', re.VERBOSE)   # Phone number
# find_phone_number = phone_number.search(text)

# Email regex
email = re.compile(r'''([a-z0-9A-Z._%+-]+    # Username
                   @                         # @ symbol
                   [a-zA-Z0-9.-]+            # Domain name
                   (\.[a-zA-Z]{2,4}))'''     # dot something
                   , re.VERBOSE)
# find_email = email.search(text)

matches = []

for groups in phone_number.findall(text):
    phoneNum = '-'.join([groups[1], groups[3]])  # add group[5] if the phone number format is 000-000-0000
    # if groups[8] != '':
    #     phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
    
for groups in email.findall(text):
    matches.append(groups[0])

# Copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone number or email found')
    
