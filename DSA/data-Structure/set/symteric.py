n=int(input())
print(n)
m=int(input())

print(m)

a=set()
b=set()

for i in range(n):
    inpu=(int)(input())
    a.add(inpu)

for i in range(m):
    ans=(int)(input())
    b.add(ans)    
    

for i in a.symmetric_difference(b):
    print(i)
# print(output)
