n1=int(input('enter the value'))
n2=int(input("enter the value"))
c=0
while True:
    s2=str(n1)
    if s2==s2[::-1]:
        c+=1
    if n1==n2-1:
        break
    n1+=1
    i=n1
print(c)
