a=input().split()

buf=[]

for i in a:
    if i not in buf:
        buf.append(i)

for i in buf:
    print(int(i),end=' ')
