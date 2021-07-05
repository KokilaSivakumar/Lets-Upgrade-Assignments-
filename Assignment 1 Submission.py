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


x = np.arange(0,10)
y = x*x
x


# In[3]:


y


# In[4]:


x = np.arange(0,10)
y = x*x
plt.plot(x,y,'go--', linewidth=2,markersize=12)
plt.title('Line Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')


# In[ ]:


#DAY 1 
# ASSIGNMENT QUESTION NO: 2


# In[7]:


x = [1,2,3,4,5,6,7] #days of week
y = [160,150,140,145,175,165,180] #sales #Assignment 2
#plt.plot(x,y)
plt.plot(x,y,'r-', linewidth=2,markersize=12)
plt.title('Sales Of The Week')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
#plt.show()


# In[ ]:


#ASSIGNMENT COMPLETED 

