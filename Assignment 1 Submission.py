#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Lets_Upgrade  -  Batch 1 | All Details | Data Visualization using Python Essentials | JUL 2021  


# In[ ]:


#Date: 5th July 2021 

#Name:       KOKILA S
#USERNAME:   @kokila_s  


# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib as mpl
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


#DAY 1 
# ASSIGNMENT QUESTION NO: 1


# In[2]:


a=np.arange(40,50)
b=np.arange(50,60)
a


# In[3]:


b


# In[10]:


a=np.arange(40,50)
b=np.arange(50,60)
plt.plot(a,b,'bo--', linewidth=2,markersize=12)
plt.title('Line Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')


# In[ ]:


#DAY 1 
# ASSIGNMENT QUESTION NO: 2


# In[22]:


days = [1,2,3,4,5,6,7] #days of d week
sales_1 = [160,150,140,145,175,165,180] #sales of company1
sales_2 = [70,90,160,150,140,145,175]  #sales of company2

#plt.plot(x,y)
plt.plot(days,sales_1,'ro-', linewidth=2,markersize=12)  #sales of company1
plt.plot(days,sales_2,'bo-', linewidth=2,markersize=12)   #sales of company2
plt.title('Sales between comapny 1 & 2')
plt.xlabel('Days of the week')
plt.ylabel('Sales')
#plt.show()


# In[ ]:


#DAY 1 
# ASSIGNMENT QUESTION NO: 3


# In[29]:


x = [1,2,3,4]
y1 = [4,3,2,1]
y2 = [10,20,30,40]
y3 = [40,30,20,10]
y4 = [1,2,1,2]
y5 = [40,70,90,70]
plt.subplot(2,2,1)
plt.plot(x,y1,'r-')
plt.subplot(2,2,2)
plt.plot(x,y2,'g*-')
plt.subplot(2,2,3)
plt.plot(x,y3,'bo-')
plt.subplot(2,2,4)
plt.plot(x,y4,'r*-')


# In[ ]:


#ASSIGNMENT COMPLETED 

