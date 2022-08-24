n=(int)(input("Enter The number"))
# 2,3,5,7,11,13,17




flag=True
for i in range(2,n ,+1)  :
    if  (n%i)==0 :
     print("Number is not  prime")
     flag=False
     break
     
     
if(flag==True) :
     print("Number is  prime")

     
     


    

   