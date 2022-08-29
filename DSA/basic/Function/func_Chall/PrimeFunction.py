
def prime(num):
    
    for i in range(2,num,+1):
        if num%i==0 :
            return False  
    return True




num1=(int)(input("Enter The  First Range  Number"))
num2=(int)(input("Enter The End Range Number"))

for i in range(num1,num2,+1):
    if(prime(i)==True):
        print("\n",i,end='')

