#reverse of a string
n=int(input())
if n>0:
    result=0
    while n>0:
        r=n%10
        result = (result*10)+r
        n = n//10
    print(result)
elif n==0:
    print(n)
else:
    result=0
    n=n*-1
    while n>0:
        r=n%10
        result = (result*10)+r
        n = n//10
        print(result*-1)