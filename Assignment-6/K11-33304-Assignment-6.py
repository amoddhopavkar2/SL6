#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('AirQualityUCI.csv',sep = ';')


# In[3]:


df.head()


# In[7]:


df.columns


# In[8]:


df.drop(['Unnamed: 15', 'Unnamed: 16'],inplace=True,axis=1)


# In[9]:


df.head()


# In[10]:


#Find out missing rows
is_NaN = df.isnull()
row_has_NaN = is_NaN.any(axis=1)
rows_with_NaN = df[row_has_NaN]


# In[ ]:





# In[15]:


df.dropna(inplace=True) #Dropping missing columns


# In[16]:


df.head()


# In[17]:


#Combining Date and Time
df['Time Stamp'] = df['Date'] + ' ' +df['Time'] 


# In[19]:


df.drop(['Date','Time'],axis=1,inplace=True)


# In[20]:


df.head()


# In[29]:


df['Time Stamp'] = pd.to_datetime(df['Time Stamp'], format='%d/%m/%Y %H.%M.%S')


# In[30]:


df.head()


# In[31]:


df.index = df['Time Stamp']


# In[34]:


df.drop('Time Stamp',axis=1,inplace=True)


# In[44]:


df.head()


# In[39]:


df['CO(GT)'] = df['CO(GT)'].str.replace(',', '.').astype(float)
df['C6H6(GT)'] = df['C6H6(GT)'].str.replace(',', '.').astype(float)


# In[43]:


df['T'] = df['T'].str.replace(',', '.').astype(float)
df['RH'] = df['RH'].str.replace(',', '.').astype(float)
df['AH'] = df['AH'].str.replace(',', '.').astype(float)


# In[45]:


for col in df.columns:
    df[col] = df[col].astype(float)


# In[48]:


df.describe()


# In[49]:


df.corr()


# In[54]:


train = pd.DataFrame(df['AH'])


# In[55]:


train['T'] = df['T']


# In[56]:


train.head()


# In[58]:


from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest = train_test_split(train['AH'],train['T'])


# In[61]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(xtrain.reshape(1,-1),ytrain)
model.predict(xtest)


# In[63]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




