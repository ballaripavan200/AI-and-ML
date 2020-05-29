v = 0;  
c = 0;  
s = 0;
str=input("enter the string")
str = str.lower();  
for i in range(0,len(str)):     
    if str[i] in ('a',"e","i","o","u"):  
        v += 1;  
    elif (str[i] >= 'a' and str[i] <= 'z'):  
        c += 1;
    else:
        s+=1
        
print("Total number of vowel and consonant are" );  
print(v);  
print(c);
print(s)
