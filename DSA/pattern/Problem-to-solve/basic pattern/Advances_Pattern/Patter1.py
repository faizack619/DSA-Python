# Pattern to form
# 12345
# 1234
# 123
# 12
# 1

n=(int)(input("Enter the number to print the pattern"))

for row in range(1,n+1) :
    
    for col in range(1,n+2-row) :
        print(col,end='')

    print()   