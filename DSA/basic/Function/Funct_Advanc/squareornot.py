from multiprocessing.sharedctypes import Value


def check(n):
    value=0
    for i in range(1,n):
        value=i*i
        if(n==value):
            return True
    else :
            return False       




n=(int)(input())
if check(n):
    print("It is perfet square")
else :
    print("It is not Perfet Square")    