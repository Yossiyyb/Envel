#!/usr/bin/env python
# coding: utf-8

# In[66]:


import pandas as pd
import datetime


# Importing data

# In[121]:


data_10_2019=pd.read_csv('C:\\Users\\yossi\\OneDrive\\Documents\\envel\\Statement_Template (2).csv', delimiter = ',')


# In[ ]:


converting date of month to proper date


# In[122]:


import datetime
for i in range(len(data_10_2019)):
   data_10_2019['Day of the month'][i] =datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, data_10_2019['Day of the month'][i])


# In[123]:


print(data_10_2019)


# In[75]:


meat = ['burgers','steak','chicken','tuna']
alcohol = ['beer','wine','scotch']
tabacco = ['malboro','camel']


# The value of the tax on each type would be determined by the "challange" the user opts into.  
# <br> Its followed by a start and end date

# In[76]:


meat_tax=[0.13,'1/10/2019','30/10/2019']
alcohol_tax=[0.2,'1/7/2019','31/8/2019']
tabacco_tax =[.5,'1/8/2019','31/12/2050']


# we check to see which transactions took place during the time that each of these challanges was taking place

# In[134]:


meat_tax_timing=(pd.to_datetime(meat_tax[1])<=data_10_2019['Day of the month'])&(pd.to_datetime(meat_tax[2]) >=data_10_2019['Day of the month'])
alcohol_tax_timing=(pd.to_datetime(alcohol_tax[1])<=data_10_2019['Day of the month'])&(pd.to_datetime(alcohol_tax[2]) >=data_10_2019['Day of the month'])
tabacco_tax_timing=(pd.to_datetime(tabacco_tax[1])<=data_10_2019['Day of the month'])&(pd.to_datetime(tabacco_tax[2]) >=data_10_2019['Day of the month'])


# we determine how much charity you need to give for each cause

# In[136]:


meat_monthly_tax=sum(data_10_2019[meat_tax_timing & data_10_2019['Item'].isin(meat)]['Cost'])*meat_tax[0]
alcohol_monthly_tax=sum(data_10_2019[alcohol_tax_timing & data_10_2019['Item'].isin(alcohol)]['Cost'])*alcohol_tax[0]
tabacoo_monthly_tax=sum(data_10_2019[tabacco_tax_timing & data_10_2019['Item'].isin(tabacco)]['Cost'])*tabacco_tax[0]


# In[137]:


print(meat_monthly_tax)
print(alcohol_monthly_tax)
print(tabacoo_monthly_tax)

