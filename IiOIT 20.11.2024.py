import sympy
from sympy import Matrix

a=Matrix([
    [ 4, 1,-6, 1,-1],
    [ 0, 5, 2,-3, 7],
    [-3, 2,-6, 2, 9],
    [ 0, 2,-4,-4, 0]
])

'''
4x1+x2-6x3+x4=-1
5x2+2x3-3x4=7
-3x1+2x2-6x3+2x4=9
2x2-4x3-4x4=0
'''

a, _ = a.rref()

j=-1
b=[[0 for i in range(5)]for j in range(4)]
for i in range(len(a[:])):
    if i%5==0:
        j+=1
    b[j][i%5]=a[i]
for i in b:
    print(i)

for i in range(len(b)):
    f=0
    for j in range(len(b[i])):
        if b[i][j]!=0 and j!=4:
            print(f'x{i+1}={b[i][-1]}')
            f=1
        elif j==4 and f == 0:
            print(f'x{i+1}=0')

#print(dir(sympy))