n=int(input())

field=[['1']*n]*n
def verger(field, i):
    j=0
    while field[i][j]!='1': j+=1
    print(j)
    for l in range(len(field[i])):
        if l!=j: field[i][l]='0'
    for k in range(len(field[i])):
        if k!=i: field[k][j]='0'
    field[i][j]='1'
    return field

def diag(field, i):
    j=0
    while field[i][j]!='1': j+=1
    print(j)
    for k in range(len(field[0])): field[(i+k)%(len(field[0]))][(j+k)%(len(field[0]))]='0'
    field[i][j]='1'
    return field

for i in range(n):
    field=verger(field, i)
    for j in field:
        print(j)
    field=diag(field, i)
    
    print('------------')
