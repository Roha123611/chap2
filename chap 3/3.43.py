#3.43
import math
def hit(x1,y1,r,x2,y2):
    if(math.sqrt((x1-x2)**2+(y1-y2)**2)>r):
        print(True)
    else:
        print(False)
    return
hit(0,0,3,3,0)