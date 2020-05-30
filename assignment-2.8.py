s=input("enter the string")
n=len(s)
c=0
for i in range(0,n):
    if s[i] in ('1','2','3','4','5','6','7','8','9'):
        s1=int(s[i])
        c+=s1
print(c) 
