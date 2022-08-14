# Display 

# ****

# ****

# ****

# ****
# print("Method 2 using print\n")
# # Method 1 using print
# print("****")
# print("****")
# print("****")
# print("****")

# #Method 2 using loop
# print("Method 2 using loop with row\n")
# i=1
# row=4
# while i <= row :
#     i=i+1
#     print("****")



#Method 3 using loop

# colum=int(input("Enter the col\n"))
# row=int(input("Enter the row\n"))
# n=int(input("Enter the col \n"))
# for i in range(row) :
    
#     for j in range(colum):
        
        
#          print('*',end = '' ) 
#     print() 
 

# display 3

# *****
# ****
# ***
# **
# *
print("Method 3 using loop with row\n")
i=0
j=0

colum=int(input("Enter the col\n"))
row=int(input("Enter the row\n"))

for i in range(row) :
    if i==j :
        for j in range(colum):
        
            print('*',end = ' ' )
        else : 
            break
       
    print()
    



# Display 4

# ****
# *  *
# *  *
# ****
# i=1
# j=1
# colum=int(input("Enter the col\n"))
# row=int(input("Enter the row\n"))
# no_colum=colum-1
# no_row=row-1
# for i in range(row) :
    
#     for j in range(colum):
        
#         if (i==0 or i==no_row or j==0 or j==no_colum):
#             print('*',end = '' ) 
#         else :
#             print(' ',end = '') 

#     print() 
       

# Display 4

#     *
#    **
#   ***
#  ****   

# n=(int)(input("Enter the number to display pattern\n"))
# i=1
# j=1
# for i in range(n) :
    
#     for j in range(n):
        
#         if  j==n-i or j==n-1 :
         
#             print('*',end = '' ) 
#         else :
#             print(' ',end = '') 

#     print() 