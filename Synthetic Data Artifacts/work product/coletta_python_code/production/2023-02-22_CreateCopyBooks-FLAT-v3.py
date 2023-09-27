#!/usr/bin/env python
# coding: utf-8

# * [Reading COBOL Layouts](http://www.3480-3590-data-conversion.com/article-reading-cobol-layouts-1.html)

# # Load libraries. Requires install of 3rd party libraries Numpy, PANDAS and treelib

# In[1]:


import pandas as pd
from pathlib import Path
from treelib import Tree
import numpy as np


# # Read in CSV containing parsed IDMS schema source

# In[2]:


#copybook_data[ ['leading_whitespace','new_leading_whitespace'] ]
#metadata = pd.read_excel( '2022-12-15_IDMS_table_descriptions.xlsx', index_col=0 )
#metadata.index.name = "table_index"
#wanted_subsystem = "DISCREPANCY PROCESSING AND ACCOUNT INFORMATION INQUIRY"
#metadata[ metadata[ wanted_subsystem ] == 1 ].copy()


# In[3]:


data = pd.read_csv('2023-02-14_FSA_FARMS_schema_from_source.csv', index_col=0)
#data = pd.read_excel( "2022-12-08_PLAS_IDMS_data_structure_WITH_VALID_VALUES.xlsx", index_col=0 )


# In[4]:


# Start off with all lines commented out and bring them back in
# Only if they turn out to be un-redefined leaf nodes:
data['commented_out'] = True


# In[5]:


data.info()


# In[6]:


data['data_level'].value_counts()


# In[7]:


pd.set_option( 'display.max_rows', None )


# In[8]:


#data.groupby( 'table_name')[ 'data_level' ].value_counts().to_frame()


# In[9]:


#test_df = data[ data['table_name'] == 'CLIENT' ]


# ## List all table/record names in this schema

# In[10]:


data['table_name'].unique()


# In[11]:


data['data_level'].value_counts().sum()


# In[12]:


#data['indent_space_count'].value_counts()


# In[13]:


data.sample(10)


# # Define functions related to flattening nested structure of data elements

# In[14]:


def TreeifyElements( grp_df : pd.DataFrame ) -> Tree:
    """Build up a tree representation of the nested data element
    structure within a single given record"""

    table_name = grp_df['table_name'].unique().squeeze()
    tree = Tree()
    tree.create_node( tag = table_name, identifier = 'root' )
    
    prev_data_level = 0
    prev_nodeid = 'root'
    data_level_to_parent_nodeid_dict = { 5 : 'root' }
    
    for row in grp_df.itertuples():
        
        if row.data_level > prev_data_level:
            # save this node as the parent of all nodes who have this data level
            data_level_to_parent_nodeid_dict[ row.data_level ] = prev_nodeid
        elif row.data_level < prev_data_level:
            # erase any subparents that we know will not have further children
            data_level_to_parent_nodeid_dict = \
                { level : node_id for level, node_id in data_level_to_parent_nodeid_dict.items() if level <= row.data_level }

        parent_id = data_level_to_parent_nodeid_dict[ row.data_level ]
        tree.create_node(
            tag = row.field_name,
            identifier = row.Index,
            parent = parent_id,
            data = row.data_level
        )
        prev_nodeid = row.Index
        prev_data_level = row.data_level

    return tree


# In[15]:


def UncommentLeafElements( grp_df : pd.DataFrame ) -> pd.DataFrame:
    """Uses the tree structure of the elements listed within a record
    to flatten out the element structure within a record for the purposes
    of defining a logical data model.
    
    Elements that are "leaf nodes" within the nested element structure
    are unnested and promoted to the top level, i.e., given a data level
    of "05". Elements that are REDEFINED are removed from the model."""

    grp_df = grp_df.copy()
    tree = TreeifyElements( grp_df )

    overwrite_these = grp_df['REDEFINES'].dropna().values

    delete_these = grp_df.index[ grp_df['field_name'].isin( overwrite_these ) ]

    for delete_this_node in delete_these:
        tree.remove_node( delete_this_node )

    leaf_indices = [ _.identifier for _ in tree.leaves() ]
    
    # Add any non-leaf elements that have 88 valid values underneath them
    all_nodes = [ tree[ nodeid ] for nodeid in tree.expand_tree() ]
    named_value_nodes = [ _ for _ in all_nodes if _.data == 88 ]
    parent_nodes_of_named_values = set( [ tree.parent( _.identifier ).identifier for _ in named_value_nodes ] )
    
    wanted_indices = leaf_indices + list( parent_nodes_of_named_values )

    grp_df.loc[ wanted_indices, 'commented_out' ] = False
    
    # not necessary since all lines start off as False
    #grp_df[ 'commented_out' ] = grp_df[ 'commented_out' ].fillna( True )
    
    named_value_node_indices = [ _.identifier for _ in named_value_nodes ]
    non_88_leaf_node_indices = list( set( wanted_indices ) - set( named_value_node_indices ) )

    # print( "*" * 100 )
    # print( "wanted_indices len=", len(wanted_indices), wanted_indices )
    # print( "named_value_nodes len=", len(named_value_nodes), named_value_nodes )
    # print( "non_88_leaf_nodes len=", len(non_88_leaf_node_indices), non_88_leaf_node_indices )
    # print()
    # print( "before:\n",  grp_df[ 'data_level' ].value_counts() )

    grp_df.loc[ non_88_leaf_node_indices, 'data_level' ] = 5
    
    # print( "after:\n",  grp_df[ 'data_level' ].value_counts() )
    # print()
    
    return grp_df


# In[16]:


#test_tree = TreeifyElements( test_df )


# In[17]:


#mod_test_df = UncommentLeafElements( test_df )


# In[18]:


#mod_test_df


# In[19]:


def Create_Copybook_Parts( grp : pd.DataFrame ) -> pd.DataFrame:
    """Massages the input spreadsheet. Takes one record's worth of
    elements at a time and formats the component strings and gets them
    ready for concatenation."""
    
    grp = UncommentLeafElements( grp )
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
    comment_column = np.where( grp['commented_out'], '*', ' ' )
    #indent = 1 + ( grp['indent_space_count'].astype( int ) - 2 ) * 4
    #indent_spaces = indent.apply( lambda i: " " * i )
    indent_spaces = grp['indent_space_count'].apply( lambda i: " " * i )
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
        #redefines_clauses = formatted_cols[ 'REDEFINES' ],
        redefines_clauses = [ "" for _ in range( len( grp ) ) ],
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


# In[20]:


data.shape


# In[21]:


formatted_df = data.groupby( 'table_index' ).apply( Create_Copybook_Parts )


# In[22]:


formatted_df.shape


# In[23]:


formatted_df.info()


# # Begin concatenating copybook syntax components

# In[24]:


#formatted_df


# In[25]:


formatted_df['first_part'] = \
    formatted_df['step_numbers'] + \
    formatted_df['comment_column'] + \
    formatted_df['indent_spaces'] + \
    formatted_df['data_level'] + \
    formatted_df['sep'] + \
    formatted_df['field_name']


# In[26]:


#formatted_df


# # Add enough space between element name and PICTURE clause to right justify text

# In[27]:


formatted_df['first_part_len'] = formatted_df['first_part'].apply( len )


# In[28]:


#formatted_df['first_part_len'].hist()


# In[29]:


(formatted_df['first_part_len'] >= 49).sum()


# In[30]:


#formatted_df['first_part_len'].describe()


# In[31]:


#long_rows = formatted_df[ formatted_df['first_part_len'] >= 49].index


# In[32]:


#formatted_df.loc[long_rows, 'first_part_len'].describe()


# In[33]:


#formatted_df['first_part'] = formatted_df['first_part'].str.ljust(50)


# In[34]:


formatted_df['white_space_middle_part'] = formatted_df['first_part_len'].apply( lambda l: (" " * (50 - l)) if l < 49 else " " )


# In[35]:


formatted_df['white_space_middle_part'].values


# # Add copybook syntax after element name, including the following clauses:
# 
# * "OCCURS" and "REDEFINES" clauses go before PIC clause
# * "VALUE" clause is either in lieu of or after PIC clause
# * COMP-3 goes after PIC clause

# In[36]:


formatted_df = formatted_df.fillna("")


# In[37]:


formatted_df.info()


# In[38]:


( (formatted_df['occurs_clauses'] != "") & (formatted_df['redefines_clauses'] != "") ).sum()


# In[39]:


#formatted_df['redefines_clauses_len'] = formatted_df['redefines_clauses'].apply( len )


# In[40]:


#formatted_df['redefines_clauses_len'].describe()


# In[41]:


#formatted_df['occurs_clauses_len'] = formatted_df['occurs_clauses'].apply( len )


# In[42]:


#formatted_df['occurs_clauses_len'].describe()


# In[43]:


# Add a separating space to the pre-pic clauses when you have both
#formatted_df.loc[ (formatted_df['occurs_clauses'] != "") & (formatted_df['redefines_clauses'] != ""), 'occurs_clauses'] = \
#    formatted_df.loc[ (formatted_df['occurs_clauses'] != "") & (formatted_df['redefines_clauses'] != ""), 'occurs_clauses'].apply( lambda s: " " + s )


# In[44]:


formatted_df['pre_pic_clause'] = formatted_df['redefines_clauses'] + formatted_df['occurs_clauses']


# ## Remove any big clumps of whitespace that make lines unnecessarily wide

# In[45]:


formatted_df[ 'pre_pic_clause' ] = formatted_df[ 'pre_pic_clause' ].str.replace( pat=r'\s+', repl=' ', regex=True )


# In[46]:


formatted_df['second_part'] = formatted_df['pre_pic_clause']


# # Diagnostic: show me some examples where a data element has an OCCURS clause or a REDEFINES CLAUSE

# In[47]:


formatted_df.loc[ (formatted_df['occurs_clauses'] != "") | (formatted_df['redefines_clauses'] != ""), 'second_part'].values[:50]


# In[48]:


#formatted_df.loc[ (formatted_df['occurs_clauses'] != "") & (formatted_df['redefines_clauses'] != ""), 'first_and_second_part'].values[:50]


# In[49]:


formatted_df['second_part_len'] = formatted_df['second_part'].apply( len )


# In[50]:


formatted_df['second_part_len'].describe()


# In[51]:


pd.set_option( 'display.max_colwidth', None )


# In[52]:


( formatted_df['pre_pic_clause'] != "" ).sum()


# In[53]:


# Add a separating space to the pic clauses when you have a pre-pic clause
formatted_df.loc[ (formatted_df['pre_pic_clause'] != "") & (formatted_df['pic_clauses'] != ""), 'pic_clauses'] = \
    formatted_df.loc[ (formatted_df['pre_pic_clause'] != "") & (formatted_df['pic_clauses'] != ""), 'pic_clauses'].apply( lambda s: " " + s )


# In[54]:


formatted_df['second_and_third_part'] = formatted_df['second_part'] + formatted_df['pic_clauses']


# # Training clauses are COMP and VALUE

# In[55]:


#formatted_df['comp_clause']


# In[56]:


formatted_df['comp_clause'].value_counts()


# In[57]:


formatted_df.loc[ (formatted_df['comp_clause'] == 'DISPLAY'), 'comp_clause' ] = ''


# In[58]:


formatted_df.loc[ (formatted_df['comp_clause'] == 'COND'), 'comp_clause' ] = ''


# In[59]:


formatted_df.loc[ (formatted_df['comp_clause'] == 'CONDITION-NAME'), 'comp_clause' ] = ''


# In[60]:


formatted_df['value_clauses'].value_counts()


# In[61]:


( (formatted_df['comp_clause'] != "") & (formatted_df['value_clauses'] != "") ).sum()


# In[62]:


# Add a separating space to the post-pic clauses when you have both
formatted_df.loc[ (formatted_df['comp_clause'] != "") & (formatted_df['value_clauses'] != ""), 'value_clauses'] = \
    formatted_df.loc[ (formatted_df['comp_clause'] != "") & (formatted_df['value_clauses'] != ""), 'value_clauses'].apply( lambda s: " " + s )


# In[63]:


formatted_df['post_pic_clauses'] = formatted_df['comp_clause'] + formatted_df['value_clauses']


# In[64]:


# Add a separating space to the pic clauses when you have a post-pic clause
formatted_df.loc[ (formatted_df['post_pic_clauses'] != "") & ((formatted_df['pre_pic_clause'] != "") | (formatted_df['pic_clauses'] != "")), 'post_pic_clauses'] = \
    formatted_df.loc[ (formatted_df['post_pic_clauses'] != "") & ((formatted_df['pre_pic_clause'] != "") | (formatted_df['pic_clauses'] != "")), 'post_pic_clauses'].apply( lambda s: " " + s )


# In[65]:


#formatted_df.loc[formatted_df['post_pic_clauses'] != "", 'post_pic_clauses'].values


# In[66]:


formatted_df[ 'second_and_third_part' ].values[:50]


# In[67]:


formatted_df[ 'second_third_and_forth_part'] = formatted_df[ 'second_and_third_part' ] + formatted_df['post_pic_clauses']


# In[68]:


formatted_df[ 'second_third_and_forth_part'].sample(50).values


# In[69]:


formatted_df[ 'second_third_and_forth_part_len'] = formatted_df[ 'second_third_and_forth_part' ].apply( len )


# In[70]:


formatted_df[ 'second_third_and_forth_part_len'].describe()


# In[71]:


formatted_df['content_len'] = formatted_df['first_part_len'] + formatted_df[ 'second_third_and_forth_part_len'] + 2 # separating space + period


# # Diagnostic: show me the widest lines, because they're not supposed to be wider than 72 characters

# In[72]:


formatted_df['content_len'].sort_values().tail(30)


# In[73]:


formatted_df.info()


# ## If the line is too wide, cut down on the whitespace in the middle for right justifying the PIC clauses, etc.

# In[74]:


formatted_df['alternative_white_space_middle_part'] = [ " " * ( 72 - _ ) for _ in formatted_df['content_len'].values ]


# In[75]:


formatted_df['alternative_white_space_middle_part_len'] = formatted_df['alternative_white_space_middle_part'].apply( len )


# In[76]:


formatted_df['alternative_white_space_middle_part_len'].describe()


# In[77]:


formatted_df.loc[ formatted_df['alternative_white_space_middle_part'] == "", 'alternative_white_space_middle_part' ] = " "


# In[78]:


formatted_df['alternative_white_space_middle_part_len'] = formatted_df['alternative_white_space_middle_part'].apply( len )


# In[79]:


formatted_df['alternative_white_space_middle_part_len'].describe()


# In[80]:


#formatted_df['alternative_white_space_middle_part_len']


# In[81]:


formatted_df['white_space_middle_part_len'] = formatted_df['white_space_middle_part'].apply( len )


# In[82]:


(~(formatted_df['white_space_middle_part_len'] < formatted_df['alternative_white_space_middle_part_len'])).sum()


# In[83]:


formatted_df['white_space_middle_part'] = formatted_df['white_space_middle_part'].where( 
    cond = formatted_df['white_space_middle_part_len'] < formatted_df['alternative_white_space_middle_part_len'],
    other = formatted_df['alternative_white_space_middle_part']
)


# In[84]:


(formatted_df[ 'second_third_and_forth_part_len'] == 0).sum()


# # Add the period to the end of each line and we're done!

# In[85]:


formatted_df[ 'line_completion' ] = '.'


# In[86]:


formatted_df[ 'line_completion' ] = formatted_df[ 'line_completion' ].where(
    cond = formatted_df[ 'second_third_and_forth_part' ] == "",
    other = formatted_df['white_space_middle_part'] + formatted_df[ 'second_third_and_forth_part' ] + '.'
)


# In[87]:


formatted_df[ 'full_line'] = formatted_df['first_part'] + formatted_df[ 'line_completion' ]


# In[88]:


formatted_df[ 'full_line_len' ] = formatted_df[ 'full_line'].apply(len)


# In[89]:


formatted_df[ 'full_line_len' ].describe()


# In[90]:


#formatted_df[ 'full_line_len' ].sort_values()


# In[91]:


#formatted_df.sort_values('full_line_len' )['full_line'].tail(50)


# # Dump the lines to a Copybook text file and give to Samee

# In[92]:


formatted_df['full_line'].to_csv("2023-02-21_IDMS_Copybooks_FARMS_FLAT_STRUCTURE.txt", header=False, index=False )


# In[93]:


get_ipython().system('head 2023-02-21_IDMS_Copybooks_FARMS_FLAT_STRUCTURE.txt')

