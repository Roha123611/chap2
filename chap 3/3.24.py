#3.24
a=int(input('enter the number you want to add to list:'))
list=[]
for i in range(0,a):
    text=str(input('enter the text to list:'))
    list.append(text)
print(list)
for a in list:
    if a=='secret':
        list.remove('secret')
print(list)