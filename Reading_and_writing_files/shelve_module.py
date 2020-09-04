import shelve

# shelfFile = shelve.open('mydata')
# cats = ['Zohie', 'Puka', 'Simon']
# shelfFile['cats'] = cats
# shelfFile.close()


shelfFile = shelve.open('mydata')
print(shelfFile['cats'])