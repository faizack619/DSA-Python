c="i am faizan"
print("Original String :-{} ".format(c))

print("Converting White Space into List",c.split())
print("Converting White Space into List with Specific Value",c.split('a'))
split=c.split()
print("Original String : ",split)
print('-'.join(split))


f="i am alpha"
for i in range(0,len(f),1):
    print(f.index(" "))
    