# N= int(input())

# x, y = [int(x) for x in input("Enter two value: ").split()]
# print("First Number is: ", x)
# print("Second Number is: ", y)
# print()
# def insert()

list=[]
v1=(int)(input())
list.append(v1)

ind,value=[int(x)for x in input("insert ").split()]
list.insert(ind,value)
ind,value=[int(x) for x in input("insert ").split()]
list.insert(ind,value)
ind,value=[int(x) for x in input("insert ").split()]
list.insert(ind,value)
list.pop()
print(list)
value=(int)(input("remove "))
list.pop(0)
print(list)
value=(int)(input("append "))
list.append(value)
print(list)
value=(int)(input("append "))
list.append(value)
print(list)

print("sort")
list.sort()
print(list)
list.pop()
print(list)
list.sort(reverse=True)
print(list)

# ind,value=(input("insert ")).split()
# value,=(int)(input())

# list.insert(ind,value)
# print(list)
# inde=(int)(input)
# v2=(int)(input)
# list.insert(inde,v2)
# # index=(int)(input)
# # list.insert(index,v2)
# # index=(int)(input)
# # list.insert(index,v2)
# print(list)
# # v3=(int)(input())
# # list.insert(1,v3)
# # print() 
