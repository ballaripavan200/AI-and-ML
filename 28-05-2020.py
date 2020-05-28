#!/usr/bin/env python
# coding: utf-8

# ### string :
# 1. " "or' '(characters) -->'a'
# 2. immutable -->we cannot change any thing
# 3. collectation of characters enclosed by cotation mark -->iterables

# In[2]:


s1 = "Hello"
s2 = 'good afternoon'
print(type(s1),type(s2))


# In[3]:


s1 = input("enter a string : ")
s2 = 'good afternoon'
print(type(s1),type(s2))


# In[4]:


# Operators : +,*(repetation),[](slice)
print(s1 + s2)#concatination
print(s1 * 3)#repittation
print(s1[2])#slicing
print(s1[-1])#slicing
print(s1[1:])#star=0,stop=length of string,step=1


# In[5]:


print(s1[0:5])
print(s1[:])


# In[6]:


#printing alternate characters
print(s1[::2])


# In[11]:


#Accept string from the user and check weather given is a palindrame or not
s3=input("enter the string :")
if s3==s3[::-1]:
    print("the given is a palindrome")
    print(":-)")
else:
    print("the given is not a palindrome")
    print(":-(")


# In[14]:


s4 = "python"
print("on"in s4)
print("xyz"in s4)
print("on"in s4)#false
print("xyz"in s4)#true


# # build in function:
# 1. len()-->length of string
# 2. max()
# 3. min()
# 4. str()

# In[22]:


s = "hello"
s1 = "abc123"
print(len(s))
print(max(s))
print(min(s))
print(str(s))
print(len(s1))
print(max(s1))
print(min(s1))
print(str(s1))


# # Built -in methord
# 1. capatilize()

# In[27]:


s = "hello"
print(len(s))#function name(object name)
print(s.capitalize)#object name.methord name()
print(s)


# In[30]:


s1 = "hellow"
s2 = "abc123"
s3 = "123"
print(s1.isalpha())#true
print(s1.isdigit())#false
print(s1.isalnum())#true
print(s2.isalpha())#true
print(s2.isdigit())#false
print(s2.isalnum())#true
print(s3.isalpha())#true
print(s3.isdigit())#false
print(s3.isalnum())#true


# s1 = "python"
# s2 = "PYTHON"

# In[36]:


n=int(input("enter the position :"))
s=input("enter the string :")
print(s.replace(s[n-1],"",1))


# # For loop
# 1. for loop with range() function
# 2. for loop with iterable object

# ````for variable_name in range(start,stop,step) :
#     statment```````

# In[40]:


n=10
for i  in range(1,n+1,1):
    print("  *  ",end=' ')
    

