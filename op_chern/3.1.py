s=input()

print(len(s))

if s[-1]=='.':
    s=s[:-1]

a=s.split()
print(len(a))

b=[]
for i in a:
    b.append(len(i))
print(min(b), max(b))

s1=''
for i in s:
    if i != '*' and i!=' ':
        s1+=2*i
    elif i==' ':
        s1+=' '
print(s1)