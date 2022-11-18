s="wWW.hACKERrANK.COM"
print("Using swapcase Function:")
print("ORIGINAL STRING- {} AND CONVERTING TO LOWER- {}".format(s,s.lower()))

print(s.swapcase())
for i in range(0,100):
    print("-",end='')
print("\nUsing Without SwapCase String")
print(len(s))

c="fAiZAn"
print("Original String",c)
print("After Swaping ")
for i in range(0,len(c),1):
    if c[i].islower():
        print(c[i].upper(),end='')
    else :
        print(c[i].lower(),end='')    
    