#3.3
#a
year=int(input('enter year to find out its leap year or not:'))
if year%4==0:
    print('could be a leap year.')
else:
    print('definitely not a leap year.')
#b
ticket=[2,3,4,6,9]
lottery=str(input('enter lottery number:'))
if lottery in ticket:
    print('you won!')
else:
    print('better luck next time!')