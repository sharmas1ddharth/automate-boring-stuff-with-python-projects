import os
my_files = ['accounts.txt', 'details.csv', 'invite.docs']

for filename in my_files:
    print(os.path.join('C:\\Users\\siddharth', filename))