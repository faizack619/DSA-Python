from math import sqrt

def hypo(a,b):
    
    c=sqrt(a ** 2 + b ** 2)
    return c

def payth(a,b,c):
    aa=max(a,b,c)
    bb=0
    cc=0

    if aa==a :
        bb=b
        cc=c
    elif aa==b:
        bb=a
        cc=c
    else :
        bb=a
        cc=b
    if (aa*aa)==(bb*bb+ cc*cc):
        return True
    else:
        return False         


x=(int)(input())  
y=(int)(input())  
z=(int)(input())  
if payth(x,y,z)==True :
    print("it is pyth")
else :
    print("It is not")    
# z=hypo(x,y)
# print(z)

   

