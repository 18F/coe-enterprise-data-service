#!/usr/bin/env python
# coding: utf-8

# # Parsing IDMS schema syntax
# 
# * [primer](https://www.sfu.ca/sasdoc/sashtml/idms/z0979730.htm)
# * [IDMS schema and subschema syntax](https://manualzz.com/doc/o/rziew/ca-idms-database-administration-guide-schema-and-subschema-compilers)
# 
# 
# ## syntax components
# * areas
# * records - table
# * elements - field
# * sets

# In[1]:


get_ipython().system('head IDMS_schema_source/ASL300.SCHEMA.FARMS.TXT')


# In[2]:


pwd


# In[3]:


get_ipython().system('wc -l  IDMS_schema_source_ALL/*')


# In[4]:


import pandas as pd
from pathlib import Path
import re
from collections import Counter


# In[5]:


#test_path = 'IDMS_schema_source/ASL300.SCHEMA.FARMS.TXT'
test_path = 'IDMS_schema_source_ALL/RMS-SCHEMA-020623.txt'


# In[6]:


lines_df = pd.read_csv( test_path, header=None )


# In[7]:


lines_df.columns = [ 'raw_line' ]


# In[8]:


lines_df[ 'stripped' ] = lines_df[ 'raw_line' ].str.slice( start = 5 )


# In[9]:


lines_df[ 'stripped' ] = lines_df[ 'stripped' ].str.rstrip()


# In[10]:


lines_df[ 'stripped' ]


# In[11]:


stripped_whitespace_file = "2023-02-03_IDMS_schema_source_stripped.txt"


# In[12]:


lines_df[ 'stripped' ].to_csv( stripped_whitespace_file, header=False, index=False )


# In[13]:


raw_text = Path( stripped_whitespace_file ).read_text()


# In[14]:


raw_text[:4]


# In[15]:


p = re.compile( r'\nADD\n' )


# In[16]:


components = p.split(raw_text )


# In[17]:


len( components )


# In[18]:


# remove the initial ADD
components[0] = components[0][4:]


# In[19]:


p = re.compile( r'^(\S+)' )


# In[20]:


p.match( components[0] ).group(1)


# In[21]:


component_categories = [ p.match( _ ).group(1) for _ in components ]


# In[22]:


c = Counter( component_categories )


# In[23]:


c.most_common()


# # Analyze Record components

# In[24]:


record_components = [ c for t, c in zip( component_categories, components ) if t == "RECORD" ]


# In[25]:


#print( record_components[0] )


# In[26]:


redefines_pattern = re.compile( r'REDEFINES' )
occurs_pattern = re.compile( r'OCCURS' )


# In[27]:


column_names = [ 'indent', 'data_level', 'element_name', 'raw_element_descriptors' ]
element_search_pat = re.compile( r'^(\s+)?(\d\d) (\S+)\n\s+(.*?)\n\s+\.', flags=re.MULTILINE | re.DOTALL )


# In[28]:


record_name_pat = re.compile( r'RECORD NAME IS (\S+)' )


# In[29]:


IS_pat = re.compile( r' IS ' )


# In[30]:


def DescriptorsSplitter( raw_descriptor_string ):
    
    descriptors = [ _.strip() for _ in raw_descriptor_string.split( '\n' ) ]
    
    key_value_pairs = [ IS_pat.split( _ ) for _ in descriptors ]
    try:
        index, values = zip( *key_value_pairs )
    except:
        # empty series
        print( "\t\tproblem splitting these characteristics" )
        print( key_value_pairs )
        retval = pd.Series( dtype='object')
    else:
        retval = pd.Series( values, index=index )
    #print( retval )
    return retval


# In[31]:


def FormatRecord( component_text, debug=False ):
    
    if debug:
        print( "*" * 50 )
    record_name = record_name_pat.match( component_text ).group(1)
    data_elements = element_search_pat.findall( component_text )
    if debug:
        print( "record", record_name, "has", len( data_elements ), "elements." )
    data_elements = pd.DataFrame( data_elements, columns = column_names )
    data_elements['record'] = record_name
    data_elements['data_step'] = [ (1+int(_)) * 100 for _ in data_elements.index ]
    data_elements['indent'] = data_elements['indent'].apply( len )
    data_elements['raw_element_descriptors'] = \
        data_elements['raw_element_descriptors'].str.replace( redefines_pattern, 'REDEFINES IS' )

    data_elements['raw_element_descriptors'] = \
        data_elements['raw_element_descriptors'].str.replace( occurs_pattern, 'OCCURS IS' )
    
    modifiers_df = data_elements['raw_element_descriptors'].apply( DescriptorsSplitter )
    
    data_elements = pd.concat( (data_elements, modifiers_df), axis=1 )
    
    data_elements = data_elements.set_index( 'record', append=True )
    return data_elements


# In[32]:


pd.set_option( 'display.max_rows', 100 )


# In[33]:


#FormatRecord( record_components[0] )


# In[34]:


pivoted_record_data = pd.concat( [ FormatRecord(_) for _ in record_components ] )


# In[35]:


pivoted_record_data.info()


# In[36]:


#pivoted_record_data.sample(100)


# In[37]:


p = re.compile( r'SCHEMA NAME IS (\S+) VERSION IS (\d+)' )


# In[38]:


p.search( components[0] ).groups()


# In[39]:


def ScrapeRecordsAndElements( schema_source_path ):

    print( "=" * 50 )
    lines_df = pd.read_csv( schema_source_path, header=None )
    lines_df.columns = [ 'raw_line' ]
    lines_df[ 'stripped' ] = lines_df[ 'raw_line' ].str.slice( start = 5 )
    lines_df[ 'stripped' ] = lines_df[ 'stripped' ].str.rstrip()

    stripped_whitespace_file = Path( schema_source_path ).with_suffix( ".formatted.txt" )
    print( "writing", f'"{ str(stripped_whitespace_file) }"' )
    lines_df[ 'stripped' ].to_csv( stripped_whitespace_file, header=False, index=False )
    raw_text = stripped_whitespace_file.read_text()

    add_pat = re.compile( r'\nADD\n' )
    components = add_pat.split( raw_text )

    #len( components )
    # remove the initial ADD
    components[0] = components[0][4:]
    
    schema_name_ver_pat = re.compile( r'SCHEMA NAME IS (\S+) VERSION IS (\d+)' )
    schema_info = schema_name_ver_pat.search( components[0] ).groups()
    schema_name, schema_version = schema_info

    first_word_pat = re.compile( r'^(\S+)' )
    component_categories = [ first_word_pat.match( _ ).group(1) for _ in components ]
    c = Counter( component_categories )

    print( schema_info, "\n", c.most_common() )

    # Analyze Record components

    record_components = [ c for t, c in zip( component_categories, components ) if t == "RECORD" ]
    
    pivoted_record_data = pd.concat( [ FormatRecord(_) for _ in record_components ] )
    pivoted_record_data = pivoted_record_data.swaplevel().sort_index()
    return pivoted_record_data
    


# In[40]:


retval = ScrapeRecordsAndElements( 'IDMS_schema_source_ALL/FARMS-V1-SCHEMA-020623.txt' )


# In[41]:


retval['VALUE'].value_counts()


# In[42]:


retval['VALUE'] = retval['VALUE'].str.extract( r' (\S+) ' )


# In[43]:


retval['VALUE'].value_counts()


# In[44]:


retval['data_level'].value_counts()


# In[45]:


retval['indent'].value_counts()


# In[46]:


retval['indent'] = (retval['data_level'].astype(int) // 5 )


# In[47]:


retval.loc[ retval['indent'] >= 5, 'indent' ] = 5


# In[48]:


retval['indent'] = retval['indent'] * 2


# In[49]:


retval['indent'].value_counts()


# In[50]:


sorted( retval.reset_index()['record'].unique() )[:5]


# In[51]:


retval.head()


# In[52]:


retval['PICTURE'] = retval['PICTURE'].str.strip()


# # Add data formatting to the csv output to get it ready for ingestion by 2023-01-24_CreateCopyBooks-v2

# In[53]:


table_index_dict = { table_name: i for i, table_name in enumerate( retval.index.levels[0] ) }


# In[54]:


retval = retval.reset_index( 'record', drop=False )


# In[55]:


retval['table_index'] = \
    [ table_index_dict[n] for n in retval['record'].values ]


# In[56]:


retval['table_vers'] = 1


# In[57]:


retval.info()


# In[58]:


retval.head()


# In[59]:


reformatted_retval = retval.rename( 
    columns={ 
        'record': 'table_name',
        'element_name' : 'field_name',
        'USAGE' : 'end',
        'PICTURE' : 'data_type',
        'indent' : 'indent_space_count',
        'data_step' : 'declaration_step'
    } )


# In[60]:


reformatted_retval['BLANK ON'] = ''
reformatted_retval['INDEXED BY'] = ''
reformatted_retval['OLQ'] = ''


# In[61]:


reformatted_retval = reformatted_retval.drop( columns=['raw_element_descriptors'] )


# In[62]:


reformatted_retval.to_csv( '2023-02-14_FSA_FARMS_schema_from_source.csv' )


# In[63]:


#retval.loc[ 'ACCT-DATA' ]
#retval.loc[ ('ACCT-DATA', slice(None)), : ]


# In[64]:


get_ipython().system('head -30 2023-02-14_FSA_FARMS_schema_from_source.csv')


# # Analyze sets

# In[65]:


set_components = [ c for t, c in zip( component_categories, components ) if t == "SET" ]


# In[66]:


len( set_components)


# In[67]:


print( set_components[0] )


# In[69]:


print( set_components)


# In[70]:


test_str = """        KEY IS (
            CTRY-DIGIT DESCENDING
            DTE-CK-SORT DESCENDING )"""


# In[71]:


import numpy as np


# In[72]:


key_search_pat = re.compile( r'KEY IS \(\s+(.*) \)', flags=re.MULTILINE | re.DOTALL )


# In[73]:


whitespace_search_pat = re.compile( r'\s+', flags=re.MULTILINE )


# In[74]:


print( test_str)


# In[75]:


m = key_search_pat.search( test_str )


# In[76]:


m.group(1)


# In[77]:


def FormatSet( component_text ):
    
    key_clause = None
    m = key_search_pat.search( component_text )
    if m:
        key_clause = " ".join( whitespace_search_pat.split( m.group(1) ) )
    
    lines_df = pd.DataFrame( { 'raw_line' : component_text.split( '\n' ) } )
    lines_df['indent'] = lines_df['raw_line'].str.extract( r'^(\s+)' )
    lines_df['indent'] = lines_df['indent'].fillna( "" ).apply( len )

    lines_df[ ['attribute', 'value' ] ] = lines_df['raw_line'].str.extract( r'^\s*(.+) IS (.+)' )
    
    lines_df.index.name = 'line'

    set_name = lines_df.loc[ lines_df[ 'attribute' ] == 'SET NAME', 'value' ].values[0]
    
    lines_df['set_name'] = set_name
    #lines_df = lines_df.set_index( 'set_name', append=True )
    if key_clause:
        lines_df.loc[ lines_df[ 'attribute' ] == 'KEY', 'value' ] = key_clause
    
    lines_df['group'] = np.nan
    lines_df.loc[ lines_df['indent'] == 4, 'group'] = lines_df.loc[ lines_df['indent'] == 4, 'attribute' ]
    lines_df['group'] = lines_df['group'].ffill()
    
    #print( lines_df )
    # label multiple members
    member_index = 0
    new_group = []
    new_attribute = []
    new_value = []
    for raw_line, group, indent, attribute, value in lines_df[ [ 'raw_line', 'group', 'indent', 'attribute', 'value' ] ].values:

        if "WITHIN AREA" in raw_line:
            attribute, value = raw_line.strip().rsplit( " ", 1 )
        else:
            try:
                if np.isnan( attribute ):
                    attribute = raw_line
                    value = True
            except:
                pass

        if group != "MEMBER":
            new_group.append( group )
            new_attribute.append( attribute ) 
            new_value.append( value )
            continue
        if indent == 4 and attribute == "MEMBER":
            member_index += 1
            new_attribute.append( f"MEMBER { str(member_index).zfill(2) }" )
            new_group.append( f"MEMBER {str(member_index).zfill(2)}" )
            new_value.append( value )
            continue
        if indent == 12:
            if ')' in raw_line:
                attribute = value = None
            else:
                attribute = f"MEMBER { str(member_index).zfill(2) } KEY {raw_line.strip()}"
                value = True
                
        new_group.append( f"MEMBER {str(member_index).zfill(2)}" )
        new_attribute.append( attribute )
        new_value.append( value )

        
    lines_df[ 'attribute' ] = new_attribute
    lines_df[ 'group' ] = new_group
    lines_df[ 'value' ] = new_value
    
    # label attributes as owner or member
    relevant_rows = lines_df['indent'] == 8
    lines_df.loc[ relevant_rows, 'attribute' ]  = lines_df.loc[ relevant_rows, 'group' ] + " " + lines_df.loc[ relevant_rows, 'attribute' ]
    
    wanted_rows = (lines_df['indent'] <= 8) & ( ~lines_df['attribute'].isna() )
    
    #try:
    #    lines_df = lines_df.loc[ wanted_rows ].pivot( columns = 'attribute', values = 'value', index = 'set_name' )
    #except ValueError:
    #    print( lines_df )
    #    raise
                   
    return lines_df
    


# In[ ]:


print( set_components[7] )


# In[ ]:


FormatSet( set_components[7] )


# In[ ]:


pivoted_data = pd.concat( [ FormatSet(_) for _ in set_components ] )


# In[ ]:


pivoted_data


# In[ ]:


#pivoted_data = pivoted_data[ sorted( pivoted_data.columns ) ]


# In[ ]:


pivoted_data.to_excel( '2023-02-07_Farms_Set_Data.xlsx' )


# In[ ]:


pwd


# In[ ]:




