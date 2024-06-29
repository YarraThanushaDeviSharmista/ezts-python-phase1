t=int(input())
for i in range(t):
 s=input()
 d={}
for i in s:
    if i in d:
       if d[i]>=2:
          print(i)
          
