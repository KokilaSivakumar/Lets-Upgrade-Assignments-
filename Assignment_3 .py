#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Assignment 3
#Question 1
#Plot using sns.relplot, line plot, box plot on fmri data set


# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
#matplotlib inline


# In[2]:


data = sns.load_dataset('fmri')
data.head()


# In[3]:


data.describe().transpose()


# In[4]:



sns.relplot(data=data,x='timepoint',y='signal',hue ='event',size='event',kind ='line')
plt.show()


# In[7]:


sns.relplot(data = data,y='signal',x='timepoint',kind='line',hue='subject',size='region')
plt.show()


# In[8]:


sns.relplot(data = data, x = 'timepoint', y = 'signal', hue= 'region')
plt.show()


# In[9]:


sns.boxplot(data = data, x = 'timepoint', y = 'signal', hue = 'region')
plt.show()


# In[10]:


sns.boxplot(data = data, x = 'timepoint', y = 'signal', hue = 'event')
plt.show()


# In[11]:



sns.lineplot(y='signal',x='timepoint',data=data)


# In[12]:


sns.lineplot(x='timepoint',y='signal',hue='event',data= data)


# In[13]:


sns.lineplot(x='timepoint',y='signal',hue='region',data=data,style='event')


# In[14]:


z=data.query("region == 'frontal'")
sns.lineplot(data=data.query("region == 'frontal'"),x="timepoint", y="signal", hue="event", units="subject",estimator=None, lw=1)


# In[15]:



sns.lineplot(y='signal',x='timepoint',hue='region',data=z,style='event')


# In[16]:


sns.lineplot(data=data, x="timepoint", y="signal", hue="event", err_style="bars", ci=50)


# In[17]:


sns.lineplot(data=data,x="timepoint", y="signal", hue="event", style="event",markers=True, dashes=False)

