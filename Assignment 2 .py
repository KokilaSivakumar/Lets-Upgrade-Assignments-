#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
from numpy.random import randn, randint, uniform, sample


# In[3]:


# ASSIGNMENT DAY-2
# Create a dataframe with 10 rows on random numbers and 4 columns, (columns labelled as a,b,c,d) and plot a bar chart.


# In[4]:


dff = pd.DataFrame(randn(10,4), columns = ["a","b","c","d"])
dff


# In[5]:


dff.plot(kind="bar", figsize=(10,10))
plt.show()


# In[ ]:




