'''
import pyperclip
a = pyperclip.paste() 
print(a)
'''

'''
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
message = phoneNumRegex.search('My number is 415-555-4242.')
# message.groups()
areacode, number = message.groups()

print(areacode)
'''

'''
import re
batRegex = re.compile(r'bat(wo)?man')
mo1 = batRegex.search('The adventures of batman')
str = mo1.group()
print(str)
'''
'''
import re
phone = re.compile(r'(\d\d)? \d{10}')
searh = phone.search('My number is +91 7830205284')
p = searh.group()
print(p)
'''

# import re
# text = re.compile(r'Bat((wo){3})man')
# search = text.search('Batwowowoman')
# if search == None:
#     print('no result')
# else:
    
#     a = search.group()

#     print(a)

# 

'''
while True:
    
    try:
        a = int(input())
        if a == 100:
            print('ji')
        else:
            print(a)
    except:
        print('enter')
        
'''


'''
import os

print(os.path.join('usr', 'bin', 'spam'))
'''

'''
import os
my_files = ['accounts.txt', 'details.csv', 'invite.docs']

for filename in my_files:
    print(os.path.join('C:\\Users\\siddharth', filename))

'''
"""
import mycats
print(mycats.cats)
print(mycats.cats[0]['name'])
"""

# def count_substring(string, sub_string):
#     for i in range(0, len(string)):
#         print(string[i])
    
#     return

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)

# string = 'I am an Indian, by birth.'
# substring = 'Birth'

# if substring in string:
#     print(string.count(substring))

# str = 'Hello World. Hello TutorialKart.'
 
#substring
# substr = 'Hello'
 
#finding number of occurrences of substring in given string

#  = 'wWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
# S = '1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
# for i in range(len(s)):
#     a = s[i].isdigit()
#     print(a)
'''
print(any(char.isalnum() for char in s))
print(any(char.isalpha() for char in s))
print(any(char.isdigit() for char in s))
print(any(char.islower() for char in s))
print(any(char.isupper() for char in s))
'''


'''
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    '''
'''  
import textwrap

text = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
wrapper = textwrap.TextWrapper(width=4)
word = wrapper.wrap(text = text)

for i in word:
    print(i)
'''

'''
import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width = max_width)
    paragraph = wrapper.wrap(text = string)

    # for i in paragraph:
    #     a = print(i)
    pa = '\n'.join(paragraph)
    return pa

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
'''

'''
x = 1
y = 1
z = 1
n = 2

ls = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
print(ls)
'''
'''
# n = int(input())
a = [-57,57]
a.sort()
print(f'sort(){a}')
# print(f'sorted{sorted(a)}')
'''

'''
student = []
score_lst = []
for i in range(int(input())):
    name = input()
    score = float(input())
    temp = []
    temp.append(name)
    temp.append(score)
    student.append(temp)
    score_lst.append(score)


score_lst = list(dict.fromkeys(score_lst))
score_lst.sort()

if len(student) >= 2:
    lowest_score_students = []
    lowest_score = score_lst[1]
    for i in student:
        if lowest_score in i:
            lowest_score_students.append(i[0])
        else:
            pass
    print('\n'.join(sorted(lowest_score_students, key=lambda lowest_score_students: lowest_score_students)))

else:
    print(student[0][0])


'''
'''
students = []
score_list = []

for _ in range(int(input())):

    temp = []

    name = input()
    score = float(input())

    temp.append(name)
    temp.append(score)

    score_list.append(score)
    students.append(temp)

score_list = list(dict.fromkeys(score_list))
score_list.sort()

if len(students) >= 2:
    second_lowest_students = []
    second_lowest_score = score_list[1]

    for i in students:
        if second_lowest_score in i:
            # print(i[0])
            second_lowest_students.append(i[0])
        else:
            pass
    print('\n'.join(sorted(second_lowest_students, key=lambda second_lowest_students: second_lowest_students)))

else:
    print(students[0][0])

'''

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

query_marks = student_marks[query_name]

total = 0

for i in query_marks:
    total += i

average_score = total / len(query_marks)
print("{:.2f}".format(average_score))

