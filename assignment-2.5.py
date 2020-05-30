n1=int(input("enter the first input"))
n2=int(input("enter the first input"))
n3=int(input("enter the first input"))
if(n1>n3 and n1>n2):
    if n2<n3:
        print("median is",n3)
    else:
        print("median is",n2)
if(n2>n3 and n2>n1):
    if n1<n3:
        print("median is",n3)
    else:
        print("median is",n1)
if(n3>n1 and n3>n2):
    if n2<n1:
        print("median is",n1)
    else:
        print("median is",n2) 
