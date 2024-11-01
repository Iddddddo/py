import math

x=1
step=0.1
a,b,c=map(int,input('a b c = ').split())
while x<5:
    if x<2:
        y=a+b*x+c*x*x
    elif x<3:
        y=(a*math.sin(x-b))**2
    elif x<4:
        y=(abs(a*b*x**3))**(1/2)+c
    else:
        y=a*math.log(abs(b+c/(2*x)))
    x+=step
    print(x, y)