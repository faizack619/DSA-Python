
def fact(n):
    fact_NUM=1
   
    for i in range(n,1,-1):
        fact_NUM*=i
         
    return fact_NUM     

    
num=(int)(input("Enter the number"))  
r=(int)(input("Enter the r")) 

print("Factorial of given number is ",fact(num))
print("r in crn factorail",fact(r))

ans=fact(num)/(fact(r)*fact(num-r))
print(ans)


