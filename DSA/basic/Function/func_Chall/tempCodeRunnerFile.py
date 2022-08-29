
def fact(n):
    fact_NUM=1
   
    for i in range(n,1,-1):
        fact_NUM*=i
         
     
    print(fact_NUM) 
    return -1

    
num=(int)(input("Enter the number"))  
r=(int)(input("Enter the r")) 

fact(num)

ans=fact(num)/fact(r)*fact(num-r)
print(ans)


