# if __name__ == '__main__':
#     N = int(input())
#     # Lists in Python - Hacker Rank Solution START
#     Output = [];
#     for i in range(0,N):
#         ip = input().split();
#         if ip[0] == "print":
#             print(Output)
#         elif ip[0] == "insert":
#             Output.insert(int(ip[1]),int(ip[2]))
#         elif ip[0] == "remove":
#             Output.remove(int(ip[1]))
#         elif ip[0] == "pop":
#             Output.pop();
#         elif ip[0] == "append":
#             Output.append(int(ip[1]))
#         elif ip[0] == "sort":
#             Output.sort();
#         else:
#             Output.reverse();
list=[1,2,3,4,]

print(list)
list.append(20)
print(list)
list.append(20)
print(list)
# list[2].append(90)
print(len(list))
coun=0
total=0
for i in list :
    coun=coun+1
    print(i,end=' ')    
print("\n",coun)    