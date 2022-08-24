n=(int)(input("Enter the number\n"))
reversedd=0
while n>1 :
    reminderr=n%10 #get Reminder 
    # print(reminderr)
    reversedd=reminderr*10
    n=n/10

print(reversedd)