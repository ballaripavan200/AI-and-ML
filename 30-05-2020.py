#!/usr/bin/env python
# coding: utf-8

# In[10]:


n=int(input("enter the number :"))
sum=n**2
sum1=(str(sum)[::-1])
sum2=int(str(n)[::-1])**2
print(sum1)
print(sum2)
if(sum1 == sum2):
    print(" given number is a adom number :")
else:
    print(" given number is not a adom number :")
    


# ### Recursivefunction
# ### Factorial of a number

# In[36]:


pro=1
n=int(input("enter any value :"))
for i in range (n,1,-1):
    pro=pro*i
print(pro)


# In[37]:


n=int(input("enter the value of n :"))
def recur_fibo(n):
    if n ==1:
        return 0
    elif n==2:
        return 1
    else:
        return recur_fibo(n-1)+recur_fibo(n-2)
prev = time.time()
print(Fibonacci(20))
print(time.time()-prev)


# In[43]:


list1 = [12,34,45,6,"str",True]
list2 = [34,45,6.6,45,[12,23,34,45,[23,34,45,6]]]
string="python"
#Len() returns no.of elements of your List
print("length of list:",len(list1))#6
#print(min(list2))
#print(max(list2))
print(list(string))
print(list1[4][1])
print(list2[4][4][3])


# In[38]:


list1 =[1,2,3,4,5]
list1.append(6)
print(list1)
list1.append(7)
print(list1)


# In[40]:


list1.insert(2,100)
print(list1)


# In[42]:


list1.extend([8,9,10])
print(list1)


# In[44]:


list1 = [23,34,56,76,68,79,80,78]
print(list1.index(34))#returns index of an element
print(list1.count(76))#frequency of an element


# In[45]:


list1.reverse()
print(list1)


# In[48]:


list1 = [1,2,3,4,5]
list2 = []
list3 = []
list2 =list1
print(list2)
list3 = list1.copy()
print(list3)
list1.append(6)
list1.append(7)
print(list1,list2,list3)


# In[ ]:




