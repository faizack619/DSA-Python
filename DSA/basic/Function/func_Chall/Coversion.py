# Binary To Decimal
def b2d(n):
    ans,y,x=0,0,1
    while n>0 :
        y=n%10
        ans=ans+x*y
        print(ans)
        x=x*2
        n=n//10
    # return ans    
    
def b2O(n):
    ans,y,x=0,0,1
    while n>0 :
        y=n%10
        ans=ans+x*y
        x=x*8
        n=n//10
    return ans   
    

n=(int)(input("Enter the Number"))
Binary_to_Decimal=b2d(n)
Binary_to_octa=b2O(n)
print("Binary to Decimal",Binary_to_Decimal)
print("Binary to octa",Binary_to_octa)