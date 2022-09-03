from __future__ import print_function
from ast import Str


def check(lis,inp):
    for i in lis:
        if(i==inp):
            return True
    else :
     return False        
 
    pass

list=[1,2,3,4,'f','a']
print("Original List",list)
inp=4
if check(list,inp)==True:
    print("It is in list")
else :
    print("It is not present in list")    
valu=input("Enter the value ")
if valu in list:
    print(f"{valu} Present")
else :
    print(f"{valu} Not Present")    