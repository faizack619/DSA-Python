# def count_substring(string, sub_string):
#     cnt=0
#     print(string)
#     print(sub_string)
#     for i in range(0,len(string),1) :
#         print(string[i])
#         if string[i]==sub_string :
#             cnt+=1
#         pass
#     # return cnt
#     pass
    
        
    

# if __name__ == '__main__':
#     string = "ABCDCDC"
#     sub_string = "CDC"
    
#     count = count_substring(string, sub_string)
#     print(count)


a="alpallh"
cnt=0
substring='al'
print(a.count('al'))
print(a.index("ll"))
for i in range(0,len(a),1):
    if a.startswith(substring,i):
        cnt+=1
    pass
print(cnt)        


