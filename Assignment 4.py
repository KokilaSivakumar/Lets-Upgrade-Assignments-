#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. What is Plotly?
#    Plotly allows users to import, copy and paste, or stream data to be analyzed and visualized. 
#    For analysis and styling graphs, Plotly offers a Python sandbox (NumPy supported), datagrid, and GUI. 
#    Python scripts can be saved, shared, and collaboratively edited in Plotly.
# 2. Where is Plotly used?
#    Plotly is used to Visualise a given data. It is also used in Machine Learning and Artifitial Intelligence Feild.


# In[2]:



import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


# 3. Plot a Pie Chart of Indian Car companies market share % values (max 6 Companies market share).

share = [23.45, 18.12, 17.56, 20.45, 7.32, 4.50]
companies = ["Maruti Suzuki", "Hyundai", "Kia", "Mahindra", "Tata", "Toyota"]
data = {"company_name": companies,"market_share": share}
df = pd.DataFrame(data)
plt.pie(share, labels = companies)
plt.show()


# In[4]:


# 4. Plot a Bar Chart with India's covid-19 Active cases ( Max 10 States )

active_cases = [119867, 102523, 65335, 37526, 38178, 2687, 20170, 1357, 5787, 1402]
states = ["Maharashtra", "Kerala", "Karnataka", "Tamil Nadu", "Andhra Pradesh", "Uttar Pradesh", "West Bengal", "Delhi", "Chhattisgarh", "Rajasthan"]
data = {"active_cases": active_cases,"states": states}
df = pd.DataFrame(data)
plt.figure(figsize=(25, 5))
plt.title("Covid Status")
plt.bar(states, active_cases)
plt.show()


# In[5]:



# 5. Plot a Line Chart with India's active covid-19 case recovery (maximum 12 Months)


dates = ['May 15 2020','June 29 2020','July 29 2020','Aug 27 2020','Sept 27 2020','Oct 30 2020','Nov 30 2020','Dec 27 2020','Jan 31 2021','Feb 28 2020','Mar 25 2021','Apr 27 2021']
recovered = [158056,567536,1532135,6143019,8182882,9432075,10267263,10677710,10758619,11112056,11733514,17988537]
data = {"dates": dates,"recovered": recovered}
df = pd.DataFrame(data)
plt.figure(figsize=(25, 5))
plt.title("Covid Status")
plt.plot(dates, recovered)
plt.show()


# In[ ]:




