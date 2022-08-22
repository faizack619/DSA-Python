### Star Pattern
#      *
#     ***
#    *****
#   *******
#  *********
#  *********
#   *******
#    *****
#     ***
#      *

def palindromicPyramid(row):
    #Outer Loop for each row
 for i in range(0,row+1):
    # 1st inner loop for printing blank spaces in each row
    for j in range(i,row+1):
        print("",end=" ")
    # 2nd inner loop for printing increasing half in each row
    for j in range(1,i+1):
        print("*",end="")   
     # 3rd inner loop for printing decreasing half in each row
    for j in range(i-1,0,-1):
        print("*",end="")       
    # print new line character for next
    print()


 for i in range(row,0,-1):
    # 1st inner loop for printing blank spaces in each row
    for j in range(i,row+1):
        print("",end=" ")
    # 2nd inner loop for printing increasing half in each row
    for j in range(1,i+1):
        print("*",end="")   
     # 3rd inner loop for printing decreasing half in each row
    for j in range(i-1,0,-1):
        print("*",end="")       
    # print new line character for next
    print()   

n=(int)(input("Enter the Number \n"))



print("Star pattern:")
palindromicPyramid(n)
