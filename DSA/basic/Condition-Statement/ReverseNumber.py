n=(int)(input("Enter the number\n"))
reversedd=0
while n!=0 :
    reminderr=n%10 #get Reminder 
    # print(reminderr)
    reversedd=reversedd*10+reminderr
    n=n//10

print(reversedd)

