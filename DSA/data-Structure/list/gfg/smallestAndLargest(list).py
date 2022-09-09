# def lar(lis):
#     a=lis
#     for i in lis:
#         if a[i]>lis[i]:
#             print(i)


#     pass

lis=[1,3,4,44,5,6]
print(lis)
lis.sort()
a=len(lis)-1
print("Smallest Number",lis[0])
print("largest Number",lis[a])

print("\nSmallest Number using min function",min(lis))
print("largest Number using min function",max(lis))


# lar(lis)

