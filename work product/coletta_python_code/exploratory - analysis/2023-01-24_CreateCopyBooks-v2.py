#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from pathlib import Path


# In[3]:


#copybook_data[ ['leading_whitespace','new_leading_whitespace'] ]
#metadata = pd.read_excel( '2022-12-15_IDMS_table_descriptions.xlsx', index_col=0 )
#metadata.index.name = "table_index"
#wanted_subsystem = "DISCREPANCY PROCESSING AND ACCOUNT INFORMATION INQUIRY"
#metadata[ metadata[ wanted_subsystem ] == 1 ].copy()


# In[4]:


data = pd.read_excel( "2022-12-08_PLAS_IDMS_data_structure_WITH_VALID_VALUES.xlsx", index_col=0 )


# In[5]:


data = data.rename( columns={ 'indent_number': 'data_level'  } )


# In[6]:


data.shape


# In[7]:


farms_table_indices = pd.read_csv( "2023-02-01_table_indices_within_FPAC_schema.csv", index_col=0)


# In[8]:


wanted_table_indices = farms_table_indices['table_index'].to_list()


# In[9]:


farms_data = data[ data['table_index'].isin( wanted_table_indices ) ]


# In[10]:


#set( [ tuple(_) for _ in farms_data[ ['table_name','table_created_date'] ].values] )


# In[11]:


farms_data['table_name'].unique()


# In[12]:


data = farms_data


# In[13]:


data.head()


# In[14]:


len( data )


# In[15]:


data['data_level'].value_counts().sum()


# In[16]:


data['indent_space_count'].value_counts()


# In[17]:


import numpy as np


# In[18]:


data.info()


# In[19]:


data.sample(10)


# # Remove suffixes from REDEFINES values
# 
# * should have done this in previous notebook that prepared the excel file, but I'm short on time now

# In[20]:


suffix_data = pd.read_csv( '2023-01-10_IDMS_table_suffixes.csv' )


# In[21]:


suffix_data.info()


# In[22]:


suffix_data


# In[23]:


wanted_suffix_cols = [ 'table_index', 'affix_type', 'affix' ]


# In[24]:


replacements = suffix_data[ wanted_suffix_cols ].dropna().values


# In[25]:


replacements


# In[26]:


len( replacements )


# In[27]:


import re


# In[28]:


for (table_index, affix_type, remove_me) in replacements:

    selection_criterion = (data['table_index'] == table_index) & data['REDEFINES'].notna()

    n_matches_found = selection_criterion.sum()

    if n_matches_found == 0:
        continue
    print( table_index, affix_type, remove_me, "n found=", n_matches_found )

    if affix_type == 'PREFIX':
        pattern = re.compile( '^' + str( remove_me ) )
    else:
        pattern = re.compile( str( remove_me )+ '$' )

    old = data.loc[ selection_criterion, 'REDEFINES' ].copy().iloc[0]
    data.loc[ selection_criterion, 'REDEFINES' ] = data.loc[ selection_criterion, 'REDEFINES' ].str.replace( pattern, "" )
    new = data.loc[ selection_criterion, 'REDEFINES' ].copy().iloc[0]
    
    print( "\t", old, "became", new )


# In[29]:


data.info()


# In[30]:


def Create_Copybook_Parts( grp ):
    
    table_index = grp['table_index'].iloc[0]
    table_ver = grp['table_vers'].iloc[0]
    table_n_fields = len(grp)
    table_name = grp['table_name'].iloc[0]
    
    print( 'table', table_index,
          'ver', table_ver,
          'n fields =', table_n_fields,
          'name =', table_name
    )
    
    temp_index = grp.index
          
    sorted_grp = grp.sort_values( 'declaration_step' )
    step_numbers = grp['declaration_step'].astype(str).str.zfill( 6 )
    comment_column = pd.Series( [ " " for _ in range( len( grp ) ) ], index=temp_index )
    indent = 1 + ( grp['indent_space_count'].astype( int ) - 2 ) * 4
    indent_spaces = indent.apply( lambda i: " " * i )
    # indent_number
    sep = pd.Series( [ "  " for _ in range( len( grp ) ) ], index=temp_index )
    
    clauses = [ 'PIC', 'BLANK ON', 'INDEXED BY', 'OCCURS', 'OLQ', 'REDEFINES', 'VALUE' ]
    formatted_cols = {}
    for clause in clauses:
        if clause == 'PIC':
            col_name = 'data_type'
        else:
            col_name = clause
        col = grp[col_name]
        col[ col.notna() ] = col[ col.notna() ].apply( lambda t:  f'{clause} {t}' )
        formatted_cols[ col_name ] = col 
    
    formatted_data = dict(
        step_numbers=step_numbers,
        comment_column=comment_column,
        indent_spaces=indent_spaces,
        data_level = grp['data_level'].astype(str).str.zfill( 2 ),
        sep = sep,
        field_name = grp['field_name'],
        pic_clauses= formatted_cols[ 'data_type' ],
        comp_clause = grp[ 'end' ],
        value_clauses = formatted_cols[ 'VALUE' ],
        occurs_clauses = formatted_cols[ 'OCCURS' ],
        redefines_clauses = formatted_cols[ 'REDEFINES' ],
        blank_on_clauses = formatted_cols[ 'BLANK ON' ],
        indexed_by_clauses = formatted_cols[ 'INDEXED BY' ],
        olq_clauses = formatted_cols[ 'OLQ' ],
    )
    
    lengths = { len(_) for _ in formatted_data.values() }
    assert len( lengths ) == 1
    assert lengths.pop() == table_n_fields
    
    df = pd.DataFrame( formatted_data )
    
    assert len( df ) == table_n_fields, f'len( df ) = {len( df )}, table_n_fields = {table_n_fields}\n\n{formatted_data}'

    table_name_line = pd.DataFrame( columns=df.columns )
    table_name_line.loc[ 0, 'step_numbers' ] = str( 50 ).zfill( 6 )
    table_name_line.loc[ 0, 'comment_column' ] = " "
    table_name_line.loc[ 0, 'indent_spaces' ] = "" # " "
    table_name_line.loc[ 0, 'data_level' ] = '01'
    table_name_line.loc[ 0, 'sep' ] = "  "
    table_name_line.loc[ 0, 'field_name' ] = table_name
    table_name_line = table_name_line.fillna( '' )

    df = pd.concat( ( table_name_line, df ), axis=0 )
    return df
    


# In[31]:


formatted_df = data.groupby( 'table_index' ).apply( Create_Copybook_Parts )


# In[32]:


formatted_df.shape


# In[33]:


formatted_df.info()


# In[34]:


formatted_df['first_part'] = \
    formatted_df['step_numbers'] + \
    formatted_df['comment_column'] + \
    formatted_df['indent_spaces'] + \
    formatted_df['data_level'] + \
    formatted_df['sep'] + \
    formatted_df['field_name']


# In[35]:


formatted_df


# In[36]:


formatted_df['first_part_len'] = formatted_df['first_part'].apply( len )


# In[37]:


#formatted_df['first_part_len'].hist()


# In[38]:


(formatted_df['first_part_len'] >= 49).sum()


# In[39]:


#formatted_df['first_part_len'].describe()


# In[40]:


#long_rows = formatted_df[ formatted_df['first_part_len'] >= 49].index


# In[41]:


#formatted_df.loc[long_rows, 'first_part_len'].describe()


# In[42]:


#formatted_df['first_part'] = formatted_df['first_part'].str.ljust(50)


# In[43]:


formatted_df['white_space_middle_part'] = formatted_df['first_part_len'].apply( lambda l: (" " * (50 - l)) if l < 49 else " " )


# In[44]:


formatted_df['white_space_middle_part'].values


# # Copybook Syntax
# 
# * "OCCURS" and "REDEFINES" clauses go before PIC clause
# * "VALUE" clause is either in lieu of or after PIC clause
# * COMP-3 goes after PIC clause

# In[45]:


formatted_df = formatted_df.fillna("")


# In[46]:


formatted_df.info()


# In[47]:


( (formatted_df['occurs_clauses'] != "") & (formatted_df['redefines_clauses'] != "") ).sum()


# In[48]:


#formatted_df['redefines_clauses_len'] = formatted_df['redefines_clauses'].apply( len )


# In[49]:


#formatted_df['redefines_clauses_len'].describe()


# In[50]:


#formatted_df['occurs_clauses_len'] = formatted_df['occurs_clauses'].apply( len )


# In[51]:


#formatted_df['occurs_clauses_len'].describe()


# In[52]:


# Add a separating space to the pre-pic clauses when you have both
#formatted_df.loc[ (formatted_df['occurs_clauses'] != "") & (formatted_df['redefines_clauses'] != ""), 'occurs_clauses'] = \
#    formatted_df.loc[ (formatted_df['occurs_clauses'] != "") & (formatted_df['redefines_clauses'] != ""), 'occurs_clauses'].apply( lambda s: " " + s )


# In[53]:


formatted_df['pre_pic_clause'] = formatted_df['redefines_clauses'] + formatted_df['occurs_clauses']


# In[54]:


formatted_df[ 'pre_pic_clause' ] = formatted_df[ 'pre_pic_clause' ].str.replace( r'\s+', ' ' )


# In[55]:


formatted_df['second_part'] = formatted_df['pre_pic_clause']


# # Diagnostic

# In[56]:


formatted_df.loc[ (formatted_df['occurs_clauses'] != "") | (formatted_df['redefines_clauses'] != ""), 'second_part'].values[:50]


# In[57]:


#formatted_df.loc[ (formatted_df['occurs_clauses'] != "") & (formatted_df['redefines_clauses'] != ""), 'first_and_second_part'].values[:50]


# In[58]:


formatted_df['second_part_len'] = formatted_df['second_part'].apply( len )


# In[59]:


formatted_df['second_part_len'].describe()


# In[60]:


pd.set_option( 'display.max_colwidth', None )


# In[61]:


( formatted_df['pre_pic_clause'] != "" ).sum()


# In[62]:


# Add a separating space to the pic clauses when you have a pre-pic clause
formatted_df.loc[ (formatted_df['pre_pic_clause'] != "") & (formatted_df['pic_clauses'] != ""), 'pic_clauses'] = \
    formatted_df.loc[ (formatted_df['pre_pic_clause'] != "") & (formatted_df['pic_clauses'] != ""), 'pic_clauses'].apply( lambda s: " " + s )


# In[63]:


formatted_df['second_and_third_part'] = formatted_df['second_part'] + formatted_df['pic_clauses']


# ### Training clauses are COMP and VALUE

# In[64]:


formatted_df['comp_clause']


# In[65]:


formatted_df['comp_clause'].value_counts()


# In[66]:


formatted_df.loc[ (formatted_df['comp_clause'] == 'DISPLAY'), 'comp_clause' ] = ''


# In[67]:


formatted_df.loc[ (formatted_df['comp_clause'] == 'COND'), 'comp_clause' ] = ''


# In[68]:


formatted_df['value_clauses'].value_counts()


# In[69]:


( (formatted_df['comp_clause'] != "") & (formatted_df['value_clauses'] != "") ).sum()


# In[70]:


# Add a separating space to the post-pic clauses when you have both
formatted_df.loc[ (formatted_df['comp_clause'] != "") & (formatted_df['value_clauses'] != ""), 'value_clauses'] = \
    formatted_df.loc[ (formatted_df['comp_clause'] != "") & (formatted_df['value_clauses'] != ""), 'value_clauses'].apply( lambda s: " " + s )


# In[71]:


formatted_df['post_pic_clauses'] = formatted_df['comp_clause'] + formatted_df['value_clauses']


# In[72]:


# Add a separating space to the pic clauses when you have a post-pic clause
formatted_df.loc[ (formatted_df['post_pic_clauses'] != "") & ((formatted_df['pre_pic_clause'] != "") | (formatted_df['pic_clauses'] != "")), 'post_pic_clauses'] = \
    formatted_df.loc[ (formatted_df['post_pic_clauses'] != "") & ((formatted_df['pre_pic_clause'] != "") | (formatted_df['pic_clauses'] != "")), 'post_pic_clauses'].apply( lambda s: " " + s )


# In[73]:


#formatted_df.loc[formatted_df['post_pic_clauses'] != "", 'post_pic_clauses'].values


# In[74]:


formatted_df[ 'second_and_third_part' ].values[:50]


# In[75]:


formatted_df[ 'second_third_and_forth_part'] = formatted_df[ 'second_and_third_part' ] + formatted_df['post_pic_clauses']


# In[76]:


formatted_df[ 'second_third_and_forth_part'].sample(50).values


# In[77]:


formatted_df[ 'second_third_and_forth_part_len'] = formatted_df[ 'second_third_and_forth_part' ].apply( len )


# In[78]:


formatted_df[ 'second_third_and_forth_part_len'].describe()


# In[79]:


formatted_df['content_len'] = formatted_df['first_part_len'] + formatted_df[ 'second_third_and_forth_part_len'] + 2 # separating space + period


# In[80]:


formatted_df['content_len'].sort_values().tail(30)


# In[81]:


formatted_df.info()


# In[82]:


formatted_df['alternative_white_space_middle_part'] = [ " " * ( 72 - _ ) for _ in formatted_df['content_len'].values ]


# In[83]:


formatted_df['alternative_white_space_middle_part_len'] = formatted_df['alternative_white_space_middle_part'].apply( len )


# In[84]:


formatted_df['alternative_white_space_middle_part_len'].describe()


# In[85]:


formatted_df.loc[ formatted_df['alternative_white_space_middle_part'] == "", 'alternative_white_space_middle_part' ] = " "


# In[86]:


formatted_df['alternative_white_space_middle_part_len'] = formatted_df['alternative_white_space_middle_part'].apply( len )


# In[87]:


formatted_df['alternative_white_space_middle_part_len'].describe()


# In[88]:


formatted_df['alternative_white_space_middle_part_len']


# In[89]:


formatted_df['white_space_middle_part_len'] = formatted_df['white_space_middle_part'].apply( len )


# In[90]:


(~(formatted_df['white_space_middle_part_len'] < formatted_df['alternative_white_space_middle_part_len'])).sum()


# In[91]:


formatted_df['white_space_middle_part'] = formatted_df['white_space_middle_part'].where( 
    cond = formatted_df['white_space_middle_part_len'] < formatted_df['alternative_white_space_middle_part_len'],
    other = formatted_df['alternative_white_space_middle_part']
)


# In[92]:


(formatted_df[ 'second_third_and_forth_part_len'] == 0).sum()


# In[93]:


formatted_df[ 'line_completion' ] = '.'


# In[94]:


formatted_df[ 'line_completion' ] = formatted_df[ 'line_completion' ].where(
    cond = formatted_df[ 'second_third_and_forth_part' ] == "",
    other = formatted_df['white_space_middle_part'] + formatted_df[ 'second_third_and_forth_part' ] + '.'
)


# In[95]:


formatted_df[ 'full_line'] = formatted_df['first_part'] + formatted_df[ 'line_completion' ]


# In[96]:


formatted_df[ 'full_line_len' ] = formatted_df[ 'full_line'].apply(len)


# In[97]:


formatted_df[ 'full_line_len' ].describe()


# In[98]:


formatted_df[ 'full_line_len' ].sort_values()


# In[99]:


formatted_df.sort_values('full_line_len' )['full_line'].tail(50)


# In[101]:


formatted_df['full_line'].to_csv("2023-02-01_IDMS_Copybooks_FPAC_schemas.txt", header=False, index=False )


# In[103]:


get_ipython().system('head 2023-02-01_IDMS_Copybooks_FPAC_schemas.txt')


# In[104]:


get_ipython().system('wc -l 2023-02-01_IDMS_Copybooks_FPAC_schemas.txt')


# In[ ]:




