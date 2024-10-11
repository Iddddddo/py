n=int(input())
a=input().split()
for i in range(n):
    a[i]=int(a[i])
maxx=0
for i in range(n-1):
    if a[i]+a[i+1]>maxx:
        maxx=a[i]+a[i+1]
print(maxx)