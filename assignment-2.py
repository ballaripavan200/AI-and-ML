a=input("enter the string")
n=len(a)
c=0
i=0
while(i<n-1):
    if a[i]=='a' and a[i+1]=='a':
        c+=1
        i=i+1
    i+=1
print(c)
