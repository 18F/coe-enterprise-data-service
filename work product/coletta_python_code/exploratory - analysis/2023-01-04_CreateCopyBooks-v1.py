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


data.head()


# In[8]:


len( data )


# In[9]:


data['data_level'].value_counts().sum()


# In[10]:


data['indent_space_count'].value_counts()


# In[11]:


import numpy as np


# In[12]:


data.info()


# # Remove suffixes from REDEFINES values
# 
# * should have done this in previous notebook that prepared the excel file, but I'm short on time now

# In[13]:


suffix_data = pd.read_csv( '2023-01-10_IDMS_table_suffixes.csv' )


# In[14]:


suffix_data.info()


# In[15]:


suffix_data


# In[16]:


wanted_suffix_cols = [ 'table_index', 'affix_type', 'affix' ]


# In[17]:


replacements = suffix_data[ wanted_suffix_cols ].dropna().values


# In[18]:


replacements


# In[19]:


len( replacements )


# In[20]:


import re


# In[21]:


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


# In[22]:


def Create_Copybook( grp ):
    
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

    df = table_name_line.append( df )
    return df
    


# In[23]:


formatted_df = data.groupby( 'table_index' ).apply( Create_Copybook )


# In[24]:


formatted_df.shape


# In[25]:


formatted_df.info()


# In[26]:


formatted_df['first_part'] = \
    formatted_df['step_numbers'] + \
    formatted_df['comment_column'] + \
    formatted_df['indent_spaces'] + \
    formatted_df['data_level'] + \
    formatted_df['sep'] + \
    formatted_df['field_name']


# In[27]:


formatted_df


# In[28]:


formatted_df['first_part_len'] = formatted_df['first_part'].apply( len )


# In[29]:


formatted_df['first_part_len'].hist()


# In[30]:


(formatted_df['first_part_len'] >= 49).sum()


# In[31]:


formatted_df['first_part_len'].describe()


# In[32]:


long_rows = formatted_df[ formatted_df['first_part_len'] >= 49].index


# In[33]:


formatted_df.loc[long_rows, 'first_part_len'].describe()


# In[34]:


formatted_df['first_part'] = formatted_df['first_part'].str.ljust(50)


# In[35]:


formatted_df['first_part']


# In[36]:


formatted_df = formatted_df.fillna("")


# In[37]:


formatted_df['pic_clauses_len'] = formatted_df['pic_clauses'].apply( len )


# In[38]:


formatted_df['pic_clauses_len'].hist()


# In[39]:


formatted_df['first_and_second_part_len'] = formatted_df['first_part_len'] + formatted_df['pic_clauses_len']


# In[40]:


formatted_df['first_and_second_part'] = formatted_df['first_part'] + " " + formatted_df['pic_clauses']


# In[41]:


formatted_df['first_and_second_part_len'] = formatted_df['first_and_second_part'].apply( len )


# In[42]:


formatted_df['first_and_second_part_len'].hist()


# In[43]:


formatted_df['first_and_second_part_len'].describe()


# In[44]:


pd.set_option( 'display.max_colwidth', None )


# In[45]:


formatted_df['first_and_second_part'].values


# In[46]:


formatted_df.columns


# In[47]:


trailing_clause_colnames = [
    'value_clauses', 'occurs_clauses',
       'redefines_clauses', 'blank_on_clauses', 'indexed_by_clauses',
       'olq_clauses',
]


# In[48]:


trailing_clauses_df = formatted_df[ trailing_clause_colnames ]


# In[49]:


non_empty_cells = trailing_clauses_df[ trailing_clause_colnames ].values != ""


# In[50]:


trailing_clauses_nparray = trailing_clauses_df[ trailing_clause_colnames ].values.astype( str )


# In[51]:


prepended_trailing_clauses_nparray = \
    np.char.add( " ", trailing_clauses_df[ trailing_clause_colnames ].values.astype(str) )


# In[52]:


new_trailing_clauses_nparray = np.where(
    non_empty_cells,
    prepended_trailing_clauses_nparray, #if non empty
    "" #if empty
)


# In[53]:


new_trailing_clauses_nparray[ non_empty_cells ]


# In[54]:


formatted_df[ trailing_clause_colnames ] = new_trailing_clauses_nparray


# In[55]:


formatted_df[ 'trailing_clauses_joined' ] = \
    formatted_df[ trailing_clause_colnames ].apply( "".join, axis=1 )


# In[56]:


formatted_df[ 'trailing_clauses_joined_len' ] = \
    formatted_df[ 'trailing_clauses_joined' ].apply( len )


# In[57]:


sorted( list( formatted_df[ 'trailing_clauses_joined_len' ].values ) )[-10:]


# In[58]:


formatted_df[ 'trailing_clauses_joined' ] = formatted_df[ 'trailing_clauses_joined' ].str.replace( r'\s+', ' ' )


# In[59]:


formatted_df[ 'trailing_clauses_joined' ] = formatted_df[ 'trailing_clauses_joined' ].str.replace( '"\'', '\'' )
formatted_df[ 'trailing_clauses_joined' ] = formatted_df[ 'trailing_clauses_joined' ].str.replace( '\'"', '\'' )


# In[60]:


formatted_df[ 'trailing_clauses_joined_len' ] = \
    formatted_df[ 'trailing_clauses_joined' ].apply( len )


# In[61]:


sorted( list( formatted_df[ 'trailing_clauses_joined_len' ].values ) )[-10:]


# In[62]:


formatted_df.loc[
    formatted_df[ 'trailing_clauses_joined_len' ] != 0,
    'trailing_clauses_joined'
].iloc[0]


# In[63]:


formatted_df['whole_line'] = formatted_df['first_and_second_part'] + \
    formatted_df[ 'trailing_clauses_joined' ]


# In[64]:


formatted_df['whole_line_len'] = formatted_df['whole_line'].apply( len )


# In[65]:


formatted_df['whole_line_len'].describe()


# In[66]:


(formatted_df['whole_line_len'] > 79 ).sum()


# In[67]:


formatted_df['dotted_whole_line'] = formatted_df['whole_line'].str.strip() + '.'


# In[68]:


formatted_df[ 'dotted_whole_line' ] = formatted_df[ 'dotted_whole_line' ].astype( str )


# In[69]:


formatted_df[ 'dotted_whole_line' ] = formatted_df[ 'dotted_whole_line' ].str.replace( r'^"', '' )
formatted_df[ 'dotted_whole_line' ] = formatted_df[ 'dotted_whole_line' ].str.replace( r'"$', '' )


# In[85]:


formatted_df['dotted_whole_line'].to_csv("2023-01-10_Coletta_IDMS_all_scraped_copybooks.csv", header=False, index=False )


# In[71]:


formatted_df.info()


# In[72]:


formatted_df


# In[73]:


formatted_df = formatted_df[ [ 'dotted_whole_line' ] ].copy() 


# In[74]:


formatted_df


# In[ ]:





# In[75]:


formatted_df[ 'line_len' ] = formatted_df[ 'dotted_whole_line' ].apply( len )


# In[76]:


too_wide_lines = formatted_df.loc[ (formatted_df[ 'line_len' ] > 80), 'dotted_whole_line' ]


# In[77]:


too_wide_lines


# In[78]:


test_str = too_wide_lines.iloc[7]


# In[79]:


print( test_str )


# In[80]:


test_str[60:65]


# In[81]:


too_wide_lines.to_csv("too_wide.csv", header=False, index=False )


# In[82]:


get_ipython().system('head -400 too_wide.csv')


# # Next steps as of Wed Jan 11
# 
# * fix line items where valid values are listed in a single line ... expand out to multiple lines e.g. ```VALUE ['00', '19', '64', '51' THRU '55',...``` each has their own line item
# * Line items that exceed 80 characters should have continuations onto the next line.
# * Pull in table metadata "2022-12-15_IDMS_table_descriptions.xlsx" and output and organize/coallate copybooks based on PLAS sybsystems

# In[83]:


#!head -400 test.csv


# In[ ]:


get_ipython().system('wc -l test.csv')


# In[ ]:


# metadata = pd.read_excel( '2022-12-15_IDMS_table_descriptions.xlsx', index_col=0 )

# metadata[ ['table_names', 'table_vers' ]].values[:10]

# table_id_to_name_dict = dict( zip( metadata.index, metadata['table_names'].values ) )

# metadata


# In[ ]:




