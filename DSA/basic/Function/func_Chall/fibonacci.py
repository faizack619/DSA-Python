
def fibo(n):
    t1=0
    t2=1
    nextterm=0
    for i in range(0,n+1,+1):
     nextterm=t1+t2
     t1=t2
     t2=nextterm
     print(nextterm) 

num=(int)(input("Enter the number"))  
fibo(num)
