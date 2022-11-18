
import textwrap 
a="ABCDEFGHIJKLIMNOQRSTUVWXYZ"

wrapper=textwrap.TextWrapper(width=4)
word_list = wrapper.wrap(text=a)
print(word_list)  
# print(','.join(word_list))
v=','.join(word_list)
print(v)

# Print each line.
# for element in word_list:
#     print(element)



# m=1
# sp=4
# c=list(a)
# print(a)

# for i in range(len(c)):
#     if i==0:
#         continue
#     c.insert(i*5,"\n")
#     if c[i]==c[-1]:
#         break
# print(c)
# j=','.join(c)
# print(j)


        