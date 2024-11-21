a=[]
while True:
    s=input().split()
    if len(s)>0:
        a.append(s)
    else:
        break
q=[]
for j in range(len(a[0])):
    poz=0
    neg=0
    for i in range(len(a)):
        if int(a[i][j])>0:
            poz+=int(a[i][j])
        else:
            neg-=int(a[i][j])
    q.append(neg-poz)

for i in a:
    print(i)
print(q)