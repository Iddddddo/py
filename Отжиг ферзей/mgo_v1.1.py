n = int(input())

def diag(f, x, y):
    x1,y1=x+1,y-1
    x2,y2=x+1,y+1
    x3,y3=x-1,y+1
    x4,y4=x-1,y-1
    while (x1<n and y1>=0):
        f[x1][y1]='0'
        x1+=1
        y1-=1
    while (x2<n and y2<n):
        f[x2][y2]='0'
        x2+=1
        y2+=1
    while (x3>=0 and y3<n):
        f[x3][y3]='0'
        x3-=1
        y3+=1
    while (x4>=0 and y4>=0):
        f[x4][y4]='0'
        x4-=1
        y4-=1
    return f
        

f=[['1']*n]*n

for x in range(n):
    y=0
    for i in range(len(f[x])):
        if f[x][i]=='1':
            y=i
            break
    
    f[x]=['0']*n #горизонталь
    
    for j in range(n):
        f[(x+j)%n][y]='0' #вертикаль
    for i in f:
        print(i)
    f=diag(f,x,y) #диагонали
    f[x][y]='1'
    
          