
#While Loop
print("While Loop with \n")
a = 0
while a < 9:
  a += 1  
  if a == 4 :
    break #Break
  print(a)
else :
  print("\nCondition Fails\n")

i = 10
while i < 9:
  i += 1  
  if i == 3 :
    break #Break
  print(i)
else :
  print("\nCondition Fails\n")


print("\nFor Loop\n")

# For Loop
j=[1,2,3,8,90]

for x in j :
  if x == 2 :
    continue   #Continue 
  print(x)

# With Range Function
print("\nfor  Loop with range\n")
for z in range(0,9,2) :
  print(z)  
else:
  print("Finally finished!")  