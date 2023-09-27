#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path


# In[2]:


raw_text = Path( "vsd_file_attributes.txt").read_text()


# In[3]:


raw_lines = raw_text.split('\n')


# In[4]:


len( raw_lines )


# In[5]:


raw_lines[0]


# In[6]:


import re


# In[7]:


my_sep = ': Composite Document File V2 Document, Little Endian, Os: Windows, Version '


# In[8]:


p3 = re.compile( ': Composite Document File V2 Document, Little Endian, Os: Windows, Version ' )


# In[9]:


len( p3.findall( raw_text ) )


# In[10]:


[ _ for _ in raw_lines if my_sep not in _ ]


# In[11]:


filtered_vsd_text = [ _ for _ in raw_lines if my_sep in _ ]


# In[12]:


len( filtered_vsd_text )


# In[13]:


vsd_2col = [ _.split( my_sep ) for _ in filtered_vsd_text ]


# In[14]:


from collections import Counter


# In[15]:


Counter( [ len(_) for _ in vsd_2col ] )


# In[16]:


file_data = [ _[1] for _ in vsd_2col ]


# In[17]:


file_data[0]


# In[18]:


file_names = [ _[0] for _ in vsd_2col ]


# In[19]:


import datetime


# In[20]:


dates = [ datetime.datetime.fromtimestamp(Path(_).stat().st_mtime).strftime('%Y-%m-%d')  for _ in file_names ]


# In[21]:


years = [ datetime.datetime.fromtimestamp(Path(_).stat().st_mtime).strftime('%Y')  for _ in file_names ]


# In[22]:


len( dates )


# In[23]:


import pandas as pd


# In[24]:


plas_dates = pd.DataFrame( dict( PLAS_DATES = dates ) )


# In[25]:


plas_dates[ 'PLAS_DATES' ]  = pd.to_datetime(  plas_dates[ 'PLAS_DATES' ] )


# In[26]:


plas_dates[ 'PLAS_DATES' ].hist()


# # Remove some trash

# In[27]:


p4 = re.compile( ', Template.*\.vs[td]', flags=re.IGNORECASE )


# In[28]:


collapsed_file_data = [ p4.sub( "", _ ) for _ in file_data ]


# In[29]:


p4 = re.compile( ', Name of Creating Application: Microsoft Visio' )


# In[30]:


collapsed_file_data = [ p4.sub( "", _ ) for _ in collapsed_file_data ]


# In[31]:


p4 = re.compile( ', Code page: 1252' )


# In[32]:


collapsed_file_data = [ p4.sub( "", _ ) for _ in collapsed_file_data ]


# In[33]:


len( collapsed_file_data )


# # Versions

# In[34]:


versions = [ _[:4] for _ in collapsed_file_data ]


# In[35]:


Counter( versions )


# In[36]:


collapsed_file_data = [ _[4:] for _ in collapsed_file_data ]


# # Authors

# In[37]:


#set( collapsed_file_data )


# In[38]:


p6 = re.compile( 'Author: (.*?), Last Saved By' )


# In[39]:


authors = [ p6.search( _ ).group(1) if p6.search( _ ) else None for _ in collapsed_file_data ]


# In[40]:


len( authors )


# In[41]:


len( set( authors ) )


# In[42]:


set( authors )


# In[43]:


Counter( authors )


# # Last Saved By

# In[44]:


p7 = re.compile( 'Last Saved By: (.*?), Last Saved Time' )


# In[45]:


savers = [ p7.search( _ ).group(1) if p7.search( _ ) else None for _ in collapsed_file_data  ]


# In[46]:


len( savers )


# In[47]:


len( set( savers ) )


# In[48]:


set( savers )


# In[49]:


Counter( savers ).most_common()


# # sort authors by date

# In[50]:


df =  pd.DataFrame( dict(
     PLAS_DATES = plas_dates[ 'PLAS_DATES' ],
     years = years,
     authors = authors,
     savers = savers,
     file_name = file_names ))


# In[51]:


df.shape


# In[52]:


df['years'] = pd.to_numeric( df['years'] )


# In[53]:


df[ ~df['savers'].isna() ].sort_values( 'years', ascending=False ).head( 50 )


# # Robert Lovelace

# In[55]:


bobs_visios = df[ df['savers'] == 'robert.lovelace' ].sort_values( 'PLAS_DATES' )


# In[57]:


bobs_visios.tail( 15 )


# In[ ]:




