# Ther are Four Way to clear the list

# Using Clear
listt=[1,2,3,4,5,6]
print("Before Removing",listt)
listt.clear()
print("After Removing using Clear",listt)

# Using Del
listt=[1,2,3,4,5,6]
print("Before Removing",listt)
del listt[:]
print("After Removing Using Del",listt)

# Using *=0
listt=[1,2,3,4,5,6,'faizan']
print("Before Removing",listt)
listt*=0
print("After Removing Using *=0",listt)

# deleting list using reinitialization
listt=[1,2,3,4,5,6]
print("Before Removing",listt)
listt = []
print("After Removing using reinitialization",listt)
