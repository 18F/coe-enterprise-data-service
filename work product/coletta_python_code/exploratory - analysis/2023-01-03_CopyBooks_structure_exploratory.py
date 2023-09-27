#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from pathlib import Path


# In[3]:


ls ~/projects/gsa_coe/copybooks/PLAS.MISSING.CPYBOOKS.cpy/


# In[4]:


get_ipython().system('cat ~/projects/gsa_coe/copybooks/PLAS.MISSING.CPYBOOKS.cpy/PHYG3B')


# # OCCURS goes before PIC clause

# In[5]:


get_ipython().system('grep -n1 "OCCURS" PLAS.MISSING.CPYBOOKS.cpy/*')


# # REDEFINES goes before PIC clause

# In[6]:


get_ipython().system('grep -n1 "REDEFINES" PLAS.MISSING.CPYBOOKS.cpy/*')


# # VALUE is either in lieu of or after PIC clause

# In[7]:


get_ipython().system('grep -n1 "VALUE" PLAS.MISSING.CPYBOOKS.cpy/*')


# # COMP goes after PIC clause

# In[8]:


get_ipython().system('grep -n1 "COMP" PLAS.MISSING.CPYBOOKS.cpy/*')


# In[9]:


get_ipython().system('grep -n1 "COND" PLAS.MISSING.CPYBOOKS.cpy/*')


# # Read in copybooks and normalize their form across the different files

# In[4]:


copybook_dir = Path( '/Users/ccoletta/projects/gsa_coe/copybooks/PLAS.MISSING.CPYBOOKS.cpy/' )


# In[5]:


#pd.read_csv?


# In[6]:


dfs = {}
for p in copybook_dir.glob( '*' ):
    name = p.stem[:6]
    try:
        df = pd.read_csv( p, sep='\t', header=None )
    except UnicodeDecodeError as e:
        continue
    dfs[ name ] = pd.Series( df[0], name=name )


# In[7]:


len( dfs )


# In[8]:


clip_these =['PHYG0O', 'PHYG0P', 'PHYG1I',]


# In[9]:


len( "1         " )


# In[10]:


len( "4C        " )


# In[11]:


len( "7C*       " )


# In[12]:


#dfs


# In[13]:


for name, df in dfs.items():
    if name not in clip_these:
        continue
    dfs[ name ] = df.apply( lambda val: val[10:] )


# In[14]:


allrows = pd.DataFrame( dfs )


# In[15]:


allrows = allrows.melt( var_name='program', value_name='raw_line' ).dropna()


# In[16]:


allrows


# In[17]:


allrows['no_decl_num'] = allrows['raw_line'].str.slice( start=6 )


# In[18]:


no_comment_rows = allrows[ ~allrows['no_decl_num'].str.startswith( '*' ) ].copy()


# In[19]:


len( no_comment_rows ) 


# In[20]:


no_comment_rows['rstripped'] = no_comment_rows['no_decl_num'].str.rstrip()


# In[21]:


no_comment_rows['rstripped'].str.len()


# In[22]:


no_blanks = no_comment_rows[ no_comment_rows['rstripped'].str.len() != 0 ].copy()


# In[23]:


len( no_blanks) 


# In[24]:


no_copys = no_blanks[ ~no_blanks['rstripped'].str.contains( 'COPY' ) ].copy()


# In[25]:


len( no_copys )


# In[26]:


pd.set_option( 'display.max_rows', None )
pd.set_option( 'display.max_colwidth', None )


# # Generate statistics about continuation of lines

# In[27]:


no_copys['continued'] = ~(no_copys['rstripped'].str.slice( start=-1 ) == '.')


# In[28]:


continuation_lines = [ _+1 for _ in list( no_copys[ no_copys['continued'] ].index ) ]


# In[29]:


no_copys[ no_copys['continued'] ].index


# In[30]:


continuation_lines


# In[31]:


no_copys['continuation'] = False


# In[32]:


no_copys.loc[ continuation_lines, 'continuation' ] = True


# In[33]:


#no_copys['rstripped'].values


# In[34]:


stats_df = no_copys['rstripped'].str.extract( r'(\s+)(\S+)' )


# In[35]:


stats_df.columns = ['leading_whitespace', 'first_token' ]


# In[36]:


stats_df.info()


# In[37]:


stats_df['leading_whitespace'] = stats_df['leading_whitespace'].str.len()


# In[38]:


set( stats_df.index ) == set( no_copys.index )


# In[39]:


stats_df.shape


# In[40]:


no_copys.shape


# In[41]:


copybook_data = pd.concat( ( stats_df, no_copys ), axis=1 )


# In[42]:


#copybook_data


# In[43]:


copybook_data.info()


# In[44]:


non_continued = copybook_data[ copybook_data['continuation'] == False ]


# In[45]:


non_continued.shape


# In[46]:


non_continued['program'].value_counts()


# In[47]:


non_continued['leading_whitespace'].value_counts()


# In[48]:


non_continued['first_token'].value_counts()


# In[49]:


copybook_data.loc[ non_continued.index, 'PIC_index'] = non_continued['raw_line'].apply( lambda line: line.index('PIC') if 'PIC' in line else -1 )


# In[52]:


copybook_data.groupby( 'program' )['PIC_index'].value_counts()


# In[53]:


copybook_data


# # Generate statistics about indentation

# In[50]:


copybook_data.loc[ non_continued.index, 'new_leading_whitespace'] = 1 + ( non_continued['first_token'].astype( int ) // 4 )*4


# In[50]:


#copybook_data[ ['leading_whitespace','new_leading_whitespace'] ]


# In[51]:


metadata = pd.read_excel( '2022-12-15_IDMS_table_descriptions.xlsx', index_col=0 )


# In[52]:


metadata.index.name = "table_index"


# In[53]:


#wanted_subsystem = "DISCREPANCY PROCESSING AND ACCOUNT INFORMATION INQUIRY"


# In[54]:


#metadata[ metadata[ wanted_subsystem ] == 1 ].copy()


# In[55]:


data = pd.read_excel( "2022-12-08_PLAS_IDMS_data_structure_WITH_VALID_VALUES.xlsx", index_col=0 )


# In[56]:


data.shape


# In[57]:


data['indent_number'].value_counts()


# In[58]:


from collections import Counter


# In[59]:


data.head()


# In[60]:


data[ ['indent_number', 'indent_space_count'] ].value_counts()


# In[61]:


data[ ['table_index', 'declaration_step'] ].values


# In[62]:


data.head( 30 )

