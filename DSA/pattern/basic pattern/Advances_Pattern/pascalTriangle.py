

# pascal triangle Pattern
# 1
# 1 2
# 1 3 3
# 1 4 6 4
# 1 5 10 10 5

def fact(n):
    fact_NUM=1
   
    for i in range(n,1,-1):
        fact_NUM*=i
         
    return fact_NUM


n=(int)(input("Enter the number"))  

for i in range(n+1):
    for j in range(i):
        # ans=fact(i)/(fact(j)*fact(i-j))
        print(fact(i)//(fact(j)*fact(i-j)),end=' ')
    print("")    

