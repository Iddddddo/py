a=[]
while True:
    s=input().split()
    if len(s)>0:
        a.append(s)
    else:
        break
q=[]
for i in range(len(a)):
    poz=0
    neg=0
    for j in range(len(a[0])):
        if int(a[i][j])>0:
            poz+=int(a[i][j])
        else:
            neg-=int(a[i][j])
    q.append(neg-poz)
k=0
while k<len(a):
    for i in range(len(a[0])+1):
        if i<len(a[0]):
            print(int(a[k][i]), end=' ')
        else:
            print(q[k])
            k+=1