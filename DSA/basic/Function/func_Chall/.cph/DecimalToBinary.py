


def Traverse(n):
  
    rev=0
    while n!=0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
        
        print(digit)

    
       





num=(int)(input("Enter the Number"))
Traverse(num)
