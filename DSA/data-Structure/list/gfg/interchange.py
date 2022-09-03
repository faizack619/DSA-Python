#Python program to interchange first and last elements in a list
def inte(new_list):
    size=len(new_list)
    temp=new_list[0]
    new_list[0]=new_list[size-1]
    new_list[size-1]=temp
    print(new_list)
    pass

lis=[1,2,3,4,5]
print(lis)
inte(lis)