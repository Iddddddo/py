import math

r = int(input())
k=(5*r+2)**2
if k==0:
    u=math.tan(r)+math.sin(r**3)
elif k==1:
    u=r**2+(r+1)**(1/5)
else:
    u=math.e**r+2.5*(r-3)
print(u)