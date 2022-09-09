#Python program to interchange first and last elements in a list
def inte(new_list):
    size=len(new_list)
    temp=new_list[0]
    new_list[0]=new_list[size-1]
    new_list[size-1]=temp
    print(new_list)
    pass

# Using interchange using comma
def inte_comman(lis):
    lis[0],lis[1]=lis[1],lis[0]
    print(lis)
    pass

lis=[1,2,3,4,5]
print(lis)
inte(lis)
print(lis)
inte_comman(lis)