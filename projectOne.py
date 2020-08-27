#!/usr/bin/env python
# coding: utf-8

# In[3]:


#check for data file
import os


# In[2]:


print(os.listdir())


# In[4]:


# import all major libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


# usage of inline plotting
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


#load data from CSV file
dataFrame = pd.read_csv('./911.csv')


# In[7]:


dataFrame.info()


# In[8]:


#check head for our dataframe
dataFrame.head()


# In[10]:


#top5 zipcodes
dataFrame['zip'].value_counts().head(5)


# In[14]:


#top6 twp reaching to 911
dataFrame['twp'].value_counts().head(6)


# In[15]:


#unique reason to call 911
dataFrame['title'].nunique()


# In[22]:


# top5 specific reasons to call 911
# assignment was there!
dataFrame['SpecificReason'] = dataFrame['title'].apply(lambda title: title.split(':')[0])


# In[23]:


dataFrame.head()


# In[25]:


dataFrame['SpecificReason'].value_counts().head()


# In[26]:


#plot a countplot for SpecificReason
sns.countplot(x='SpecificReason', data=dataFrame)


# In[27]:


#convert timeStamp from object to actual time stamp
dataFrame['timeStamp'] = pd.to_datetime(dataFrame['timeStamp'])


# In[29]:


dataFrame.info()


# In[30]:


type(dataFrame['timeStamp'].iloc[0])


# In[99]:


#create 3 columns for Hour, Months and day of week
dataFrame['Hour'] = dataFrame['timeStamp'].apply(lambda time: time.hour)
dataFrame['Month'] = dataFrame['timeStamp'].apply(lambda time: time.month)
dataFrame['Day'] = dataFrame['timeStamp'].apply(lambda time: time.dayofweek)


# In[102]:


dataFrame['Hour'].nunique()


# In[104]:


#plot a graph for Month
sns.countplot(x='Month', data=dataFrame, hue='SpecificReason')


# In[108]:


#use group_by 
byMonth = dataFrame.groupby('Day').count()


# In[109]:


byMonth.head()


# In[110]:


byMonth['twp'].plot()


# In[ ]:




