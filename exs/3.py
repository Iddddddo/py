n=int(input())
a=input().split()
for i in range(n):
    a[i]=int(a[i])
    
if max(a)<0:
    print(0)
else:
    for i in range(n):
        if a[i]<0:
            a[i]=10**9
    print(min(a))
    