#practice problem 2.1
#prob(a)
a=1
b=2
c=3
d=4
e=5
sum=a+b+c+d+e
print('sum of first 5 integers is:',(sum))
#prob(d)
a=403
b=73
r=a%b
print('403 is divided by 73 then reminder is:',r)
#prob(e)
a=2**10
print('2 to the 10th power is:',a)
#prob(c)
x=int(73/403)
print('no of times 73 goes into 403:',x)
#prob(g)
lst=min(34.99,29.95,31.50)
print('lower price among the three is:',lst)
#prob(f)
sara_height=54
marks_height=57
diff_h=abs(sara_height-marks_height)
print('difference between is:',diff_h)
#practice problem 2.2
#prob(a)
a=2+2<4
print('the sum of 2 and 2 is less than 4:',a)
#prob(b)
y=7//3==1+1
print('the value of 7//3 is equal to 2:',y)
#prob(c)
s=3**2+4**2==25
print('the sum of 3**2 and 4**2 is eqaul to 25:',s)
#prob(d)
t=2+4+6>12
print('the sum of 2,4,and 6 is greater than 12:',t)
#prob(e)
a=1387/19==0
print('1387 is divisible by 19:',a)
#prob(f)
b=31%2==0
print('31 is even:',b)
#prob(g)
l_p=min(34.99,29.95,31.50)<30.00
print('lowest price is less than 30.oo:',l_p)
#practice problem 2.3
#a
a=3
print(a)
b=4
print(b)
c=(a*a)+(b*b)
print(c)
#practice problem 2.4
#a
s1='ant'
s2='bat'
s3='cod'
b=s1+" "+s2+" "+s3
print(b)
n=(10*(s1+" "))
print(n)
r=(s1+" "+(2*(s2+" "))+(3*(s3+" ")))
print(r)
#d
print(7*(s1+" "+s2+" "))
#e
print(5*(s2+s3+s3+" "))
#practice problem 2.5
#a
s='0123456789'
print(s[0])
print(s[1])
print(s[6])
print(s[8])
print(s[9])
#practice problems2.6
#a
words=['bat','ball','barn','basket','badminton']
print(min(words))
print(max(words))
#practice problem 2.7
grades=[9,7,7,10,3,9,6,6,2]
print(grades.count(7))
grades[-1]=4
print(grades)
print(max(grades))
grades.sort()
print(grades)
sum=9+7+7+10+3+9+6+6+2
average=(sum/9)
print(average)
#ex2.9
#a
print(type(False+False))
#b
print(type(2*(3**2.0)))
#c
print(type((4//2)+(4%2)))
#d
print(type((2+3==4)or(5>=5)))
#ex2.11
#c
a=2**-20
print(a)
#d
b=int(61/4356)
print(b)
#e
e=4365/61
print(e)
#2.12
s1='-'
s2='+'
#a
print(s1+s2)
#b
print(s1+s2+s1)
#c
print(s2+s1+s1)
#2.18
#a
flower=['rose','bougainvilla','yucca','marigold','daylilly','lilly']
#b
print('potato' in flower)
#e
thorny=flower[0:3]
print(thorny)
#d
poisonous=flower[5:6]
print(poisonous)
#e
dangerous=thorny + poisonous
print(dangerous)
#2.17
#a
print((17-9)<10)
#b
inventory=['paper','staples','pencils']
x=len(inventory)
print(x)
full_name='john filzgerald kennedy'
y=len(full_name)
print(y)
#2.15
a='anachronistically'
b='counterintuitive'
x=b=-1