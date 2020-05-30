s1=int(input("enter the string"))
s2=str(s1)
if s2==s2[::-1]:
    print("palidrome")
else:
    while s2!=s2[::-1]:
        s3=int(s2[::-1])
        s1+=s3
        s2=str(s1)
print(s1) 
