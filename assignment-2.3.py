a=input("enter the string")
n=len(a)
c=0
i=0
while(i<n):
    if a[i]=='(':
        c+=1
    else:
        c-=1
    i+=1
if c==0:
    print(n//2)
elif c<0:
    print(") are",-c , "more")
else:
    print("( are", c ,"more" )
