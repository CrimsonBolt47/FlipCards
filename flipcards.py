

def flipcard(a):
   t,s = a[:len(a)//2], a[len(a)//2:]
   print("t-",t,"s-",s)
   k=list(t)
   m=""
   for i in range(len(k)):
        if(k[i]=="O"):
            k[i]="X"
        else:
            k[i]="O"
   print("k-",k)    
   m=m.join(k)
   t=m
   i = j = 0
   result = ""
   while i < len(s) and j < len(t):
      result += s[i] + t[j]
      i+=1
      j+=1
   while i < len(s):
      result += s[i]
      i += 1
   while j < len(t):
      result += t[j]
      j += 1
   return result

a="O"*10
k=a
"""
for j in range(10):
        a=flipcard(a)
        #if(k==a):
        print(a,j)
"""
print(flipcard(a))   


"""
for i in range(15,30):
    a="O"*i
    k=a
    print(len(a))
    for j in range(100):
        a=flipcard(a)
        if(k==a):
            print(k,j)
            """


