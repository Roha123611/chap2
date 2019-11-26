#program1
#time taken 8
#calculating the area
from math import pi
def cylinderarea(r,h):
    area =(2 * pi * r * h)+(2*pi*(r**2))
    print('the area of cylinder is:{0} cm\u00b2'.format(area))
    return
cylinderarea(3,5)
#calculate the volume
def cylindervolume(r,h):
    volume=(pi*(r**2)*h)
    print('the volume of cylinder is:{0} cm\u00b3'.format(volume))
    return
cylindervolume(2,4)
#program2
#t.taken 7min
def cylinderarea(l,w):
    area=l*w
    print('the area of rectangle is:{0} cm\u00b2'.format(area))
    return
cylinderarea(2,5)
#calculate the volume
def cylindervolume(w,l):
    volume=w*l
    print('the vol of the rectangle is:{0} cm\u00b3'.format(volume))
    return
cylindervolume(5,6)
#program4
#t.taken 10MIN
def palindrome(text):
    x=text.casefold()
    #print(x)
    y=len(text)
    #print(y)
    z=x[y::-1]
    #print(z)
    if x==z:
        print('the text is palindrome')
    else:
        print('sorry')
    return
text=str(input('enter the text to check for palindrome:'))
palindrome(text)
#program8
#t.taken 12min
def reverseName(name):
    x=len(name)
    y=name[x::-1]
    print(y)
name=str(input('enter your name:'))
reverseName(name)
#program9
def encrypt(text,step):
    outText=[]
    encryptText=[]
    uppercase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lowercase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for eachLetter in text:
        if eachLetter in uppercase:
            index=uppercase.index(eachLetter)
            encrypting=(index+step)%26
            encryptText.append(encrypting)
            newLetter=uppercase[encrypting]
            outText.append(newLetter)
        elif eachLetter in lowercase:
            index=lowercase.index(eachLetter)
            encrypting=(index+step)%26
            encryptText.append(encrypting)
            newLetter=lowercase[encrypting]
            outText.append(newLetter)
    print(outText)
    return
encrypt('hello my name is roha',3)












