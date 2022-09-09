
def su(l):
   sum=0
   for i in l:
    sum=sum+i
    
   return sum   

def mult(l):
    muli=1
    for i in l:
     muli=muli*i
     
    return muli  

def reve(l):
    size=len(l)-1
    
    print("This is list",l)
    
    for i in range(size,-1,-1):
        print(l[i],end=' ')
   
    
    pass    
    
    
l=[1,2,3,4,5,1,1]
print("Original List",l)
total=su(l)
print(total)

mu=mult(l)
print("Multiplication of lis",mu)

reve(l)
print("\n",l)

# Using Sum Function
import numpy as np
from operator import mul
print("Using In build Functionn",sum(l))
print("Using In numpy build Functionn",np.prod(l))
muli=1
for i in l:
 muli=mul(i,muli) 
print("Using In operator build Functionn",muli)


