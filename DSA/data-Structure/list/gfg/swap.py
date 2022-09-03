# Python program to swap two elements in a list
# Python | Ways to find length of list without len function
# swap first with middle



def swap(lis,size):
    
    middle=size//2
    temp=lis[0]
    lis[0]=lis[middle]
    lis[middle]=temp
    return lis

def leng(lis):
    coun=0
    for i in lis:
        coun=coun+1
    return coun    

def swapPositions(list, pos1, pos2): #Using Comma
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
 
# Driver function
List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print(swapPositions(List, pos1-1, pos2-1))

lis=[1,2,3,4,45]
print("Original List",lis)
size=leng(lis)
print("Length of list",size)    

swapping=swap(lis,size)
print("After Interchange",swapping)
