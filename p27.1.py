#prime or not
n = int(input())
for i in range(2,n+1):
    if n%i==0:
        print("Not a Prime")
else:
    print("Prime")