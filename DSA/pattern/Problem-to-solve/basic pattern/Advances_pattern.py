# Pattern to form
# 12345
# 1234
# 123
# 12
# 1

# n=(int)(input("Enter the number to print the pattern"))
# # row=1
# # col=1
# for row in range(1,n+1) :
#     # print(row)
   
#     for col in range(1,n+2-row) :
#         print(col,end='')

#     print()    

# 1
# 01
# 101
# 0101
# 10101



n=(int)(input("Enter the number to print the pattern"))

for row in range(1,n+1) :
   
    for col in range(0,row) :
        if(((row+col)%2)==0) :
            print("0",end=' ')
        else :
            print("1",end=' ')    
    print()         