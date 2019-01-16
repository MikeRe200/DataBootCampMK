
# coding: utf-8

# In[64]:


import pandas as pd
import numpy as np


# In[6]:


fileName="datasets/DC_Properties.csv"
fileDcProp=pd.read_csv(fileName)
fileDcProp


# In[ ]:


df = pd.read_csv("datasets/gradedatamissing.csv")
df.head()


# In[74]:


#df2= fileDcProp.drop('Unnamed: 0', axis=1)
#df2[['HEAT','ROOMS']]
df2=fileDcProp[['FULLADDRESS','YR_RMDL','ASSESSMENT_NBHD','SALEDATE','PRICE','QUADRANT','SALE_NUM','ROOMS']]
df2


# dupe=duplication
# df.loc[dupe]

# In[45]:


dupe=df2.duplication()

df[dupe]


# In[78]:


#Average price by Quadrant
# We can see here that in NW the price is 10x
df3=df2.groupby('QUADRANT')['PRICE'].max()
df3

df33=df2.groupby('QUADRANT')['PRICE'].max()
df33


# In[60]:


df4=df2.groupby('QUADRANT')['SALE_NUM'].mean()

df4


# In[80]:


#Number of Property Sold By Quadrant

df5=df2.groupby('QUADRANT')['SALE_NUM'].count()
df5


# In[76]:


#Number of Saled Houses per Quadrant
df6=df2.groupby('ROOMS')['SALE_NUM'].count()
df6


# In[83]:


df6=df2['PRICE'].isnull()
df6

