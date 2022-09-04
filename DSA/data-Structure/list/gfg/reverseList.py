

# Reverse A String
def rev(lis):
    siz=len(lis)-1
    for i in range(siz,-1,-1):
        print(lis[i])
    pass


lis=[1,2,3,5,6]
print(lis)

# Using List Compersion

l=[1,22,3,432,98]
print("\nOriginal lis :",l)
g=[l[i] for i in range(len(l)-1,-1,-1)]
print("\nReverse List",g)


# Using 
a=lis.reverse()
print("Using Function :",a)
rev(lis)

print("Adding in list")

b=[]
for i in lis:
    b=i
    print(b)

print("\n",lis)


# Using List Compersion

c=[i for i in lis ]


li=[1,2,3,6,7]
d=[li[len(li) - i] for i in range(1, len(li)+1)]
print("\n",d)

# Learn Compershion
import numpy as np
z=np.arange(1,11)
print("\n",z)

od=["Even" if i%2==0 else "odd"  for i in z]
print(od)

c=[i for i in range(0,10) if i <5 ]
print(c)


