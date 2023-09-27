#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data = pd.read_excel( "2022-12-08_PLAS_IDMS_data_structure_WITH_VALID_VALUES.xlsx", index_col=0 )


# In[4]:


data = data.rename( columns={ 'indent_number': 'data_level'  } )


# In[5]:


data.shape


# In[6]:


data.head()


# In[9]:


data['field_name'].value_counts().head(50)


# In[ ]:




