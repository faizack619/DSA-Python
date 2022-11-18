
n=(int)(input("enter the number  \n"))

cnt=len(str(n))
print("Length of String",cnt)

print("The Reserve number is ")
sum=0
num=n



while num>0:
    res=num%10
    sum=sum+res**cnt
    print("s :",sum,end='')
    num//=10
    print("")
    pass

print(n)
print(sum)
if n == sum :
    print("Number {} is armstrong".format(n))
else :
    print("Number {} is not Armstrong".format(n))    
    