# Rhombus pattern
#    ****
#   ****
#  ****
# ****   

n=(int)(input("Enter the number to print the pattern"))
for row in range(1,n) :
    for col in range(1,n-row):
        print("",end=" ")
    for col in range(n) :
        print("*",end="")    
    print()    


# Rhombus reverse pattern
# ****
#  ****
#   ****
#    ****   
n=(int)(input("Enter the number to print the pattern\n"))
for row in range(1,n) :
    for col in range(1,row):
        print("",end=" ")
    for col in range(n) :
        print("*",end="")    
    print()    
