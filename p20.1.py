t=int(input())
for i in range(t):
    n=int(input())
    c=0
    while n>0:
        if n%10==4:
            c=c+1
        n=n//10
    print(c)