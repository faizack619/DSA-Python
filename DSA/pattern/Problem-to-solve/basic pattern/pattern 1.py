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
 


# print("Method 3 using loop with row\n")

# colum=int(input("Enter the col\n"))
# row=int(input("Enter the row\n"))

# for i in range(0,row) :
#         for j in range(0,colum):
#             if(j==i):
#                  print('*',end = ' ' )
          

#         print()   


       
                



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

# display 3
#row =5
#col=5
# *
# **
# ***
# ****
# *****
 # outer loop to handle number of rows
    # n in this case
# n=(int)(input("Enter the number"))
# for i in range(0, n): 
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i+1):
         
#             # printing stars
#             print("* ",end="")
      
#         # ending line after each row
#         print("")   

# Half Pramid Number
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# def pypart(n):
#     for i in range(1,n+1):

#         for j in range(0,i):
#             print(i,end=" ")
#         print("\r")


# n=(int)(input("Enter the number"))
# pypart(n)

# Floyd Triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# def floyd(n):
#     sum=0
#     for i in range(1,n+1):

#         for j in range(0,i):
#             sum=sum+1
#             print(sum,end=" ")
#         print("\r")


# n=(int)(input("Enter the number"))
# floyd(n)


# Butterfly Pattern
# *
# **
# ***
# ****
# ****
# ***
# **
# *



# def halfbutterfly(n):
#     num=n*1
    
    
#     for i in range(0,num):

#         for j in range(0,i+1):
#              print("*",end=" ")

#         print()

    
#     for i in range(num+1,0,-1):

#         for j in range(0,i-1):
#              print("*",end=" ")
#         print()  


 
# n=(int)(input("Enter the number"))
# halfbutterfly(n)    


#
# Hourglass Pattern    
#    * * * * * * 
#     * * * * * 
#      * * * * 
#       * * * 
#        * * 
#         * 
#         * 
#        * * 
#       * * * 
#      * * * * 
#    * * * * * 
#   * * * * * *

# def hourglass(n) :
#     num=n*1
#     space=num-2
    
    
#     for i in range(0,num):

#         for j in range(0,i+1):

#              print("*",end=" ")

#         print()

    




n=(int)(input("Enter the number"))
hourglass(n) 