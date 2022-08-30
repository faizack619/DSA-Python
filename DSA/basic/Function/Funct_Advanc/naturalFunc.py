def sum(n):
    total=0
    for i in range(1,n+1,1):
        total+=i
    return total


num=(int)(input())  
  
s=sum(num)
print(s)