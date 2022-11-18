s = "qa@"
countnum =0
countal =0
countdigi =0
countlower =0
countUpper =0
for i in s:
   if (i.isalnum()):
     countnum +=1
    
     
   if (i.isalpha()):
     countal +=1
 
     
   if (i.isdigit()):
     countdigi +=1
    
     
   if (i.islower()):
     countlower +=1
     
     
   if (i.isupper()):
     countUpper +=1
     

if countnum >0:
  print(True)
else :
  print(False)

if countal >0:
  print(True)
else :
  print(False)     

if countdigi >0:
  print(True)
else :
  print(False)

if countlower >0:
  print(True)
else :
  print(False)  

if countUpper >0:
  print(True)
else :
  print(False)

