t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    for j in range(n):
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        c=0
        for k in range(n):
            if a[k]>=x:
                c=c+b[k]
        print(c)




