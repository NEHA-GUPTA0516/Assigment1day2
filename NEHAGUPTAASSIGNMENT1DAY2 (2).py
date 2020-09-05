#!/usr/bin/env python
# coding: utf-8

# # list and its functions

# In[19]:


lst=[1,2,3,'neha','simmi',[1,2],'neha',5,5,56]


# In[20]:


lst


# In[21]:


lst.append('100')                      #for adding any item at the end of list


# In[22]:


lst


# In[23]:


len(lst)                         #for finding out the length of list 


# In[24]:


lst.count('neha')                   #for finding the repetition or count of any or repeated data item


# In[25]:


lst.index(5)                       #for finding the index of data item


# In[26]:


lst.reverse()                        #for reversing the whole list


# In[28]:


print('lst')
lst


# In[29]:


lst.remove(5)           #for removing any object from the lsit


# In[30]:


lst


# In[31]:


lst.pop()              #for returning or remoing last or object from the list
lst.pop(5)


# # SETS AND ITS FUNCTIONS

# In[45]:


st1={"monday","tue","wed","thurs","fri","sat","sun"}


# In[46]:


st2={"monday","sun"}


# In[47]:


st2.issubset(st1)           #to check whether set2 is subset of set 1


# In[52]:


#union 
st1|st2                      


# In[54]:


#intersection
st1&st2


# In[55]:


#difference

st1-st2


# In[57]:


st2.add('tue')              #to add more element in set


# In[58]:


st2


# # DICTIONARIES

# In[1]:


dit={"name":"neha","sem":"3rd","rollno":"70"}
print(dit)


# In[3]:


dit.get("name")                    #to get any object from the dict 


# In[4]:


len(dit)                                                                       #for finnding length of dict


# In[5]:


dit2={"name":"sonali","sem":"3rd","rollno":"71"}
print(dit2)


# In[17]:


dit3=dit2.copy()                                                                       #for copying same dict
print ("the new dictionary %s :" % str(dit2))


# In[22]:


dit.items()                                                  #for getting all the   items of dict


# In[23]:


dit4={"age":"19"}                                                #for adding new key and valu to the required dict
dit.update(dit4)
print(dit)


# # tuples

# In[24]:


tup=(1,2,3,4,55,5,6,5,7,8,8)
print(tup)


# In[25]:


tup.count(5)
                                             #to count the length of tuple


# In[26]:


tup.index(3)                                             #to get the index of item or objeCT


# In[39]:


tup2=(25,45)
max(tup2)               #for getting maximum vALUE


# In[40]:


min(tup)                                #for getting minimum value


# In[50]:


lst = [1, 'neha', 'simmi', 'abc',5]
atup = tuple(lst)
print (" tuple elements : ", atup)                                         #for converting list into tuples


# # STRINGS

# In[1]:


a="hello neha!"


# In[2]:


print(a[1])


# In[3]:


print(a.lower())                                          #for converting letters to lower case


# In[4]:


print(a.upper())                                          #for converting letters to upper case


# In[5]:


print(a[1:4])                                     #slicing


# In[6]:


b="how are you ?"
print(b)


# In[10]:


c= a + " " + b                                           #for String Concatenation
print(c)


# In[11]:


d="1234"
print(d)


# In[12]:


d.isnumeric()                                                 #to check all the character in strings are number


# In[14]:


myDit = {"name": "hello", "country": "london"}                     #to join all items in a dictionary into a string
myStr = "city"

x = myStr.join(myDit)

print(x)


# # end-------
