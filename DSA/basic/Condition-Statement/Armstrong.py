from unicodedata import digit


n=(int)(input("Enter the number\n"))
arm=0
original_n=n
while n!=0 :
    lastdigit=n%10 #get Reminder 
    arm=arm+(lastdigit*lastdigit*lastdigit)
    n=n//10

print(arm)
if original_n==arm :
    print("Number is Armstrong")
else :
    print("Number is not Armstrong")