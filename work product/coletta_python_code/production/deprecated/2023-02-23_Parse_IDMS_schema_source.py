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

# # Import libraries

# In[1]:


import pandas as pd
from pathlib import Path
import re
from collections import Counter


# # List of all the IDMS subschema files we were provided

# In[2]:


pwd


# ## Do a line count for each file we received

# In[3]:


get_ipython().system('wc -l  IDMS_schema_source_ALL/*')


# # Examine the contents of one of the subschema files

# In[4]:


get_ipython().system('head -300 IDMS_schema_source_ALL/FARMS-V1-SCHEMA-020623.txt | tail -50')


# # Create some regular expressions to help us parse schema text

# In[5]:


#print( record_components[0] )


# In[6]:


redefines_pattern = re.compile( r'REDEFINES' )
occurs_pattern = re.compile( r' OCCURS ' )


# In[7]:


column_names = [ 'indent', 'data_level', 'element_name', 'raw_element_descriptors' ]
element_search_pat = re.compile( r'^(\s+)?(\d\d) (\S+)\n\s+(.*?)\n\s+\.', flags=re.MULTILINE | re.DOTALL )


# In[8]:


record_name_pat = re.compile( r'RECORD NAME IS (\S+)' )


# In[9]:


IS_pat = re.compile( r' IS ' )


# # Define parsing functions

# In[10]:


def DescriptorsSplitter( raw_descriptor_string : str ) -> pd.Series:
    """This function parses the descriptors after one single data element,
    including PICTURE, USAGE, ELEMENT LENGTH, POSITION, etc. Returns a single
    row's worth of element descriptors."""

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


# In[11]:


def FormatRecord( component_text : str, debug=False ) -> pd.DataFrame:
    """Takes the raw text of one record's worth of schema definition
    and parses all data elements from it."""
    
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
    
    # Here, we add in an "IS" to REDEFINES and OCCURS descriptors to allow for
    # DescriptorSplitter() to work in a uniform way across all descriptors that
    # already use the "IS", e.g., "PICTURE", "ELEMENT LENGTH" etc.
    data_elements['raw_element_descriptors'] = \
        data_elements['raw_element_descriptors'].str.replace( redefines_pattern, 'REDEFINES IS' )

    data_elements['raw_element_descriptors'] = \
        data_elements['raw_element_descriptors'].str.replace( occurs_pattern, ' OCCURS IS ' )
    
    modifiers_df = data_elements['raw_element_descriptors'].apply( DescriptorsSplitter )
    
    data_elements = pd.concat( (data_elements, modifiers_df), axis=1 )
    
    data_elements = data_elements.set_index( 'record', append=True )
    return data_elements


# In[12]:


def ScrapeRecordsAndElements( schema_source_path : Path ) -> pd.DataFrame:
    """Takes the path of one schema source file, parses out its component parts
    including SCHEMA, AREA, RECORD, and SET, and parses each record. Output is
    a PANDAS dataframe containing parsed info."""

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


# # INPUT THE SCHEMA FILE YOU WANT TO PARSE HERE:

# In[13]:


retval = ScrapeRecordsAndElements( 'IDMS_schema_source_ALL/FARMS-V1-SCHEMA-020623.txt' )


# In[14]:


retval.info()


# In[15]:


retval.head()


# # Cleanup

# ## Cleanup item 1: remove parentheses from valid values

# In[16]:


retval['VALUE'].value_counts()


# In[17]:


retval['VALUE'] = retval['VALUE'].str.extract( r' (\S+) ' )


# In[18]:


retval['VALUE'].value_counts()


# ## Cleanup item 2: Reformat indents so copybooks look nice

# In[19]:


retval['data_level'].value_counts()


# In[20]:


retval['indent'].value_counts()


# In[21]:


retval['indent'] = (retval['data_level'].astype(int) // 5 )


# In[22]:


retval.loc[ retval['indent'] >= 5, 'indent' ] = 5


# In[23]:


retval['indent'] = retval['indent'] * 2


# In[24]:


retval['indent'].value_counts()


# ## Cleanup item 3: remove leading spaces from PICTURE clause

# In[25]:


retval['PICTURE'].values


# In[26]:


retval.head()


# In[27]:


retval['PICTURE'] = retval['PICTURE'].str.strip()


# # Add data formatting to the csv output to get it ready for ingestion by CreateCopyBooks notebook/script
# 
# Here we are just changing the tablenames of the output spreadsheet and adding dummy columns so the next script can run unedited.

# In[28]:


table_index_dict = { table_name: i for i, table_name in enumerate( retval.index.levels[0] ) }


# In[29]:


retval = retval.reset_index( 'record', drop=False )


# In[30]:


retval['table_index'] = \
    [ table_index_dict[n] for n in retval['record'].values ]


# In[31]:


retval['table_vers'] = 1


# In[32]:


retval.info()


# In[33]:


retval.head()


# In[34]:


reformatted_retval = retval.rename( 
    columns={ 
        'record': 'table_name',
        'element_name' : 'field_name',
        'USAGE' : 'end',
        'PICTURE' : 'data_type',
        'indent' : 'indent_space_count',
        'data_step' : 'declaration_step'
    } )


# In[35]:


reformatted_retval['BLANK ON'] = ''
reformatted_retval['INDEXED BY'] = ''
reformatted_retval['OLQ'] = ''


# In[36]:


reformatted_retval = reformatted_retval.drop( columns=['raw_element_descriptors'] )


# In[37]:


reformatted_retval.to_csv( '2023-02-14_FSA_FARMS_schema_from_source.csv' )


# In[38]:


#pd.set_option( 'display.max_rows', 100 )


# In[39]:


# Two Python/PANDAS syntactical ways to select one whole table for inspection, if you want
#retval.loc[ 'ACCT-DATA' ]
#retval.loc[ ('ACCT-DATA', slice(None)), : ]


# In[40]:


get_ipython().system('head -30 2023-02-14_FSA_FARMS_schema_from_source.csv')

