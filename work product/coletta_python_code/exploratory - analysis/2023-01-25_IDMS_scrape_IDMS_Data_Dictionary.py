#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path


# In[2]:


import re


# In[3]:


#!head -150 IDMS_RECORDS_cpy.txt | tail -50


# In[4]:


import pandas as pd


# In[5]:


from collections import Counter


# In[6]:


#ls


# In[7]:


pd.set_option( 'display.max_rows', 200 )


# In[8]:


#subsystems = pd.read_excel( "PLAS Subsystem Schema -Revised.xlsx", index_col=0)


# # PLAS subsystems names

# In[178]:


pwd


# In[164]:


subsystems = pd.read_excel( "PLAS Subsystem Schema -Revised.xlsx", index_col=0, sheet_name=1)


# In[165]:


wanted_columns = ['Program\nSchema', 'System Name' ]


# In[166]:


drop_these = set( subsystems.columns ) - set( wanted_columns )


# In[167]:


subsystems = subsystems.drop( columns=drop_these )


# In[168]:


subsystems.columns = ['code', 'plas_subsystem' ]


# In[169]:


subsystems[ subsystems['code'] == 'BD' ]


# In[170]:


subsystems = subsystems.drop( index = 122 )


# ## Systems without a code

# In[171]:


no_code = subsystems[ subsystems['code'] == '**' ]


# In[172]:


no_code


# In[173]:


subsystems = subsystems.drop( index = no_code.index )


# In[174]:


subsystems.shape


# In[175]:


subsystems = subsystems.dropna( subset=['code'] )


# In[176]:


subsystems.shape


# In[177]:


subsystems.sort_values( 'code' )


# In[ ]:


two_letter_code_to_subsystem_desc_map = dict( subsystems.values )


# In[ ]:


#!cp /Users/ccoletta/Library/CloudStorage/Box-Box/GSA\ USDA\ -\ CONTRACTOR\ ACCESS/PLAS_CODE_AND_DOCUMENTAION/file_lengths.txt .


# # Analysis of COBOL programs obtained in discovery (line counts for each file)

# In[ ]:


files = pd.read_csv( 'file_lengths.txt', header=None  )


# In[ ]:


files.columns = ['raw_line']


# In[ ]:


files = files['raw_line'].str.split(expand=True)


# In[ ]:


files.columns = ['line_count', 'file_path']


# In[ ]:


files['n_slashes'] = files['file_path'].str.count('/')


# In[ ]:


files['n_slashes'].value_counts()


# In[ ]:


#files['file_path'].str.contains( 'PLAS_documentation' ).value_counts()
#files = files[ ~files['file_path'].str.contains( 'PLAS_documentation' ) ].copy()
#files = files[ ~files['file_path'].str.contains( 'archive_of_archives' ) ].copy()
#files = files[ files['n_slashes'] == 2].copy()


# In[ ]:


path_parts = files['file_path'].str.split( '/', expand=True )


# In[ ]:


files[ ['file_dir', 'file_name' ] ] = path_parts[ [1,2] ]


# In[ ]:


files


# In[ ]:


files = files[ ['line_count', 'file_dir', 'file_name' ] ].copy()


# In[ ]:


files = files.reset_index(drop=True)


# In[ ]:


files['file_name_len'] = files['file_name'].apply( len ) 


# In[ ]:


files['file_name_len'].value_counts()


# In[ ]:


#tuple( two_letter_code_to_subsystem_desc_map.keys() )


# In[ ]:


files.shape


# In[ ]:


files = files.sort_values( ['file_dir', 'file_name' ] )


# In[ ]:


files


# In[ ]:


file_counts = files['file_name'].value_counts()


# In[ ]:


dupes = set( file_counts[ file_counts != 1 ].index )


# In[ ]:


multiple_places = files[ files['file_name'].isin( dupes ) ].groupby( 'file_name' )[ 'file_dir' ].agg( set )


# In[ ]:


multiple_places['ABBM08']


# ## Match COBOL filenames to their PLAS subsystem via two-letter naming convention

# In[ ]:


valid_codes = tuple( sorted( list( two_letter_code_to_subsystem_desc_map.keys() ) ) )


# In[ ]:


files['categorized'] = files['file_name'].str.startswith( valid_codes )


# In[ ]:


files['categorized'].value_counts()


# In[ ]:


files


# In[ ]:


categorized = files[ files['categorized'] ]


# In[ ]:


Counter( [ _[:2] for _ in categorized['file_name'].values ] ).most_common(n=30)


# In[ ]:


Counter( [ _[:3] for _ in categorized['file_name'].values ] ).most_common(n=30)


# In[ ]:


Counter( [ _[:4] for _ in categorized['file_name'].values ] ).most_common(n=30)


# In[ ]:


Counter( [ _[:5] for _ in categorized['file_name'].values ] ).most_common(n=30)


# In[ ]:


uncategorized = files[ ~files['categorized'] ]


# In[ ]:


uncategorized.shape


# In[ ]:


Counter( [ _[:1] for _ in uncategorized['file_name'].values ] ).most_common()


# In[ ]:


Counter( [ _[:2] for _ in uncategorized['file_name'].values ] ).most_common( 30 )


# In[ ]:


Counter( [ _[:3] for _ in uncategorized['file_name'].values ] ).most_common( 30 )


# In[ ]:


Counter( [ _[:4] for _ in uncategorized['file_name'].values ] ).most_common( 30 )


# In[ ]:


Counter( [ _[:5] for _ in uncategorized['file_name'].values ] ).most_common( 30 )


# In[ ]:


Counter( [ _[:6] for _ in uncategorized['file_name'].values ] ).most_common( 30 )


# ## Line count analysis

# In[ ]:


files['file_dir'].value_counts()


# In[ ]:


files['line_count'] = files['line_count'].astype( int )


# In[ ]:


files.info()


# In[ ]:


line_count_analysis = files.groupby( 'file_dir' )['line_count'].describe().round().astype( int )


# In[ ]:


line_count_analysis.sort_values( '50%', ascending=False )


# # Analysis/transformation of IDMS data dictionary file "IDMS_RECORDS_cpy.txt"

# ## Initial cleaning

# In[9]:


# !head -50 IDMS_RECORDS_cpy.txt

# p = Path( "2022-10-14_Whitespace_stripped.txt" )

# raw_text = p.read_text(encoding='latin1')

# len( raw_text )

# print( raw_text[:1000] )

# 

# p = re.compile( r'^1REPORT.*?^0$', flags = re.MULTILINE | re.DOTALL )

# len( p.findall( raw_text ) )

# removed_headers = p.sub( "", raw_text )

# len( removed_headers )


# In[10]:


out = Path( "2022-10-14_Stripped_IDMS_RECORDS.txt" )


# In[11]:


#out.write_text( removed_headers )


# In[12]:


# reload after some hand-editing
removed_headers = out.read_text()


# In[13]:


len( removed_headers )


# In[14]:


lines = removed_headers.split( '\n' )


# In[15]:


len( lines )


# In[16]:


p = re.compile( r'^\s+' )


# In[17]:


p.findall( lines[0] )


# In[18]:


[ i for i, _ in enumerate( lines ) if len( p.findall( _ ) ) == 0 ]


# In[19]:


lines = [ _ for _ in lines if _ != "" ]


# In[20]:


len( lines )


# In[21]:


[ i for i, _ in enumerate( lines ) if len( p.findall( _ ) ) == 0 ]


# In[22]:


leading_space_count = [ len( p.findall( _ )[0] ) for _ in lines if len( p.findall( _ ) ) > 0 ]


# In[23]:


Counter( leading_space_count )


# ## Create grouping variables based on position

# In[24]:


table_index = -1
synonym_index = -1
table_indices = [0]*len( lines )
synonym_indices = [0]*len( lines )
modifier_target_lines = [0]*len( lines )
modified_line = -1
modifier_line_prefix = " "*26

for i in range( len( lines ) ):
    if lines[i][1] != ' ':
        table_index += 1
        synonym_index = -1
    if lines[i].startswith( '     RECORD'):
        synonym_index += 1
    if modified_line < 0 and lines[i].startswith( modifier_line_prefix ):
        # first time we're seeing a modifier?
        # Record the line that is being modified
        modified_line = i - 1
    if modified_line > 0 and not lines[i].startswith( modifier_line_prefix ):
        modified_line = -1

    modifier_target_lines[ i ] = modified_line
    table_indices[ i ] = table_index
    synonym_indices[ i ] = synonym_index


# In[25]:


#table_indices


# In[26]:


len( leading_space_count ) == len( lines )


# In[28]:


lines_df = pd.DataFrame( dict(
    leading_space_count = leading_space_count,
    table_index = table_indices,
    synonym_index = synonym_indices,
    modifies_line = modifier_target_lines,
    line = lines ))


# In[29]:


lines_df.info()


# In[30]:


lines_df[ lines_df[ 'modifies_line' ] > 0]


# In[31]:


lines_df[ 'modifies_line' ].value_counts().value_counts()


# In[32]:


lines_df[ lines_df['leading_space_count'] == 1 ]


# In[33]:


text_clumps = lines_df.groupby( 'leading_space_count' ).apply( lambda group: group['line'].to_list() )


# In[34]:


text_clumps.info()


# In[35]:


[ len( _ ) for _ in text_clumps ]


# In[36]:


lines_df['synonym_index'].value_counts()


# ## TABLE NAMES

# In[ ]:


text_clumps[1][:20]


# In[ ]:


Counter( [ len(_) for _ in text_clumps[1] ] )


# In[ ]:


p = re.compile( r'\s(\S+)\s+VER\s+(\d+)' )


# In[ ]:


table_info_list = [ p.match( _ ).groups(1) for _ in text_clumps[1] ]


# In[ ]:


len( table_info_list )


# In[ ]:


table_info_list[:10]


# In[ ]:


table_names, table_vers = zip(*table_info_list )


# In[ ]:


created_dates = pd.to_datetime( [ _[101:109] for _ in text_clumps[1] ] )


# In[ ]:


len( created_dates )


# In[ ]:


updated_dates = pd.to_datetime( [ _[92:100] for _ in text_clumps[1] ], errors='coerce' )


# In[ ]:


updated_dates


# In[ ]:


table_info = pd.DataFrame( data=dict(
    table_names=table_names,
    table_vers=table_vers,
    created_dates=created_dates,
    updated_dates= updated_dates
))


# In[ ]:


table_info['created_dates'] = table_info['created_dates'].dt.date
table_info['updated_dates'] = table_info['updated_dates'].dt.date


# In[ ]:


table_info.info()


# In[ ]:


table_info.head(20)


# ## Lines beginning with 5 spaces contain table metadata

# In[107]:


text_clumps[5][:20]


# In[108]:


p = re.compile( r'     (\S+)' )


# In[109]:


Counter( [ p.match( _ ).groups(1)[0] for _ in text_clumps[5] ] )


# In[127]:


schema_df = lines_df[ (lines_df[ 'leading_space_count' ] == 5) & ( lines_df[ 'line' ].str.contains( 'IN SCHEMA' ) ) ]


# In[128]:


p = re.compile( r'IN SCHEMA\s+(\S+)\s+VER\s+(\d+)\s+AREA\s+(\S+)' )


# In[129]:


schema_df['line'].iloc[0]


# In[130]:


schema_extracts_df = schema_df['line'].str.extract( p )


# In[131]:


schema_extracts_df.columns = ['schema', 'schema_ver', 'schema_area']


# In[132]:


schema_extracts_df.shape


# In[133]:


schema_df = pd.concat( ( schema_df.copy(), schema_extracts_df ), axis = 1)


# In[134]:


schema_df


# In[159]:


schema_df


# In[162]:


schema_df['schema'].value_counts()


# In[ ]:


# DMLO data manipulation language online, 

# everything is development. 

# 20 or 30 files for history, run jobs 3 times.


# In[163]:


schema_df['subschema'].value_counts()


# ### Wanted:
# 
# FARMS
# FARMS0
# FARMS1
# FARMS2
# RMS
# SCMAC01
# SCMACCT
# SCMFA01
# SCMHN01
# SCMUA01

# In[153]:


wanted_schema = 'FARMS FARMS0 FARMS1 FARMS2 RMS SCMAC01 SCMACCT SCMFA01 SCMHN01 SCMUA01'.split()


# In[154]:


wanted_schema


# In[152]:


schema_df['schema'].value_counts().sort_index()


# In[156]:


farms_schema_df = schema_df.loc[ (schema_df['schema'].isin( wanted_schema ) ) & (schema_df['schema_ver'] =='1') ]


# In[157]:


len(farms_schema_df)


# In[158]:


farms_schema_df['table_index'].reset_index(drop=True).to_csv( '2023-02-01_table_indices_within_FPAC_schema.csv' )


# ### Pull DESCRIPTION one-liners

# In[ ]:


p = re.compile( r'^ (\S+)\s+VER\s+(\d+).*?DESCRIPTION\s+(.*?)$', flags=re.DOTALL | re.MULTILINE ) 


# In[ ]:


desc_table_names, desc_table_vers, desc_descs = zip( *p.findall( removed_headers ) )


# In[ ]:


len( desc_table_names )


# In[ ]:


len( desc_table_vers )


# In[ ]:


len( desc_table_names) 


# In[ ]:


descs = pd.DataFrame( dict(
    table_names = desc_table_names,
    table_vers = desc_table_vers,
    descriptions = desc_descs ))


# In[ ]:


table_info.shape


# In[ ]:


descs.shape


# In[ ]:


merged_table_info = table_info.merge( descs, on=['table_names', "table_vers"], how='left' )


# In[ ]:


merged_table_info


# ### Pull synonym table names, prefixes and suffixes

# In[ ]:


suffix_df = lines_df[ lines_df['leading_space_count'] == 5 ]


# In[ ]:


suffix_df.shape


# In[ ]:


suffix_df = suffix_df[ suffix_df['line'].str.startswith( '     RECORD' ) ]


# In[ ]:


suffix_df = suffix_df.copy()


# In[ ]:


suffix_df.info()


# In[ ]:


name_start_pos = 26
name_end_pos = 67
affix_type_start_pos = 80
affix_type_end_pos = 86
affix_start_pos = 87


# In[ ]:


suffix_df['synonym_name'] = [ _[26:67].strip() for _ in suffix_df['line'].values ]


# In[ ]:


suffix_df['affix_type'] = [ _[80:86] if len(_) > 80 else "" for _ in suffix_df['line'].values  ]


# In[ ]:


suffix_df['affix'] = [ _[87:] if len(_) > 80 else "" for _ in suffix_df['line'].values  ]


# #### There exists 4126 total synonyms

# In[ ]:


suffix_df.shape


# In[ ]:


suffix_df.head(40)


# In[ ]:


suffix_df.to_csv( '2023-01-10_IDMS_table_affixes.csv' )


# In[ ]:


# temp = list( suffix_df['line'] )

# temp[:5]

# temp[0][67:76]

# temp[0].index("VER")

# #p = re.compile( r' ' )

# #suffix_df.groupby( 'table_index' ).apply( , axis=1, result_type='expand' )


# ## Lines beginning with 9 spaces indicate "COPIED IN PROGRAM", "FILE", AND "SUBSCHEMA"

# ### Copied in Program analysis

# In[ ]:


#text_clumps[9][-200:]
#text_clumps[9][-20:]


# In[ ]:


p = re.compile( r'\s+(\S+)' )


# In[ ]:


Counter( [ p.match( _ ).groups(1)[0] for _ in text_clumps[9] if p.match( _ ) ] )


# In[ ]:


#sorted( [ _ for _ in text_clumps[9] if "FILE" in _ ] )


# In[ ]:


#[ _ for _ in text_clumps[9] if "LANGUAGE" in _ ]


# In[ ]:


#[ _ for _ in text_clumps[9] if "SUBSCHEMA" in _ ]


# In[ ]:


#[ _ for _ in text_clumps[9] if "COPIED" in _ ]


# In[ ]:


lines_df.info()


# In[ ]:


selection_criteria = ( lines_df['leading_space_count'] == 9 ) & lines_df['line'].str.contains( "COPIED" )


# In[ ]:


program_table_df = lines_df.loc[ selection_criteria, 'line' ].str.extract( r'(\S+)\s+VER\s+(\d+)$' )


# In[ ]:


program_table_df.columns = ['copied_in_program', 'copied_in_program_ver']


# In[ ]:


program_table_df


# In[ ]:


program_table_df = lines_df.merge( program_table_df, left_index=True, right_index=True, how='right' )


# In[ ]:


program_table_df


# #### Thirty most popular programs cited in "COPIED IN PROGRAM" statements

# In[ ]:


program_table_df['copied_in_program'].value_counts().head(30)


# In[ ]:


def GetCode( prog_name ):
    for code in valid_codes:
        if prog_name.startswith( code ):
            return code
    return None


# In[ ]:


program_table_df['subsystem'] = program_table_df['copied_in_program'].apply( GetCode )


# #### Twenty most popular subsystems cited in "COPIED IN PROGRAM" statements
# 
# 1. AU - UPDATE PROGRAMS
# 2. TS - Rural Community Facility Tracking System (RCFTS)
# 3. BA - UPDATES AND PRINTOUTS
# 4. AD - DISCREPANCY PROCESSING AND ACCOUNT INFORMATION
# 5. AW - ONLINE LOAN HISTORY
# 6. LQ - REPACK BORROWERS FILE [Food repack facilities?](https://naturalchoicefoods.com/private-label-frozen-food-repacker/)
# 7. AR - STATE/COUNTY FILE CHANGES
# 8. FF - TERMINAL APPLICATION
# 9. DB - DATABASE MAINTENANCE - IDMS-DC USERS PASSWORD
# 10. ER - ACCOUNT STATUS

# In[ ]:


subsystem_counts = program_table_df['subsystem'].value_counts().to_frame()


# In[ ]:


subsystem_counts = subsystem_counts.reset_index()
subsystem_counts.columns = ['code', 'subsystem_table_count' ]


# In[ ]:


table_subsystem_counts = subsystem_counts.merge( subsystems )


# In[ ]:


table_subsystem_counts


# In[ ]:


program_table_df


# In[ ]:


table_to_program_map = program_table_df.groupby( 'table_index' )['copied_in_program'].agg( lambda x: sorted( list( set( x ) ) ) )


# In[ ]:


table_to_program_map.name = 'program_list'


# In[ ]:


table_to_program_map


# In[ ]:


per_table_program_count = table_to_program_map.apply( len )


# In[ ]:


per_table_program_count.name = 'per_table_program_count'


# In[ ]:


table_to_program_map = pd.concat( ( table_to_program_map, per_table_program_count ), axis=1 )


# #### Twenty tables most COPIED IN PROGRAM
# 
# Big winner: table 220

# In[ ]:


table_to_program_map.sort_values( "per_table_program_count", ascending=False ).head( 20 )


# In[ ]:


table_to_subsystem_map = program_table_df.dropna( subset=['subsystem'] ).groupby( 'table_index' )['subsystem'].agg( lambda x: sorted( list( set(x) ) ) )


# In[ ]:


table_to_subsystem_map


# In[ ]:


per_table_subsystem_count = table_to_subsystem_map.apply( len )


# In[ ]:


per_table_subsystem_count.name = "per_table_subsystem_count"


# In[ ]:


table_to_subsystem_map = pd.concat( ( table_to_subsystem_map, per_table_subsystem_count ), axis=1 )


# #### Twenty most cross-functional tables
# 
# Winners:
# * 2067
# * 220
# * 743
# * 771

# In[ ]:


table_to_subsystem_map.sort_values("per_table_subsystem_count", ascending=False).head(20)


# #### Any letter code patterns in the for the programs without subsystems?
# 
# Important patterns:
# 
# * IMD* - 5162
# * S?DLD* - 14149
# * BGD* - 753

# In[ ]:


no_subsystem_categorization = program_table_df.loc[ program_table_df['subsystem'].isna(), 'copied_in_program' ]


# In[ ]:


no_subsystem_categorization.str.slice( stop=1 ).value_counts().head(20)


# In[ ]:


no_subsystem_categorization.str.slice( stop=2 ).value_counts().head(20)


# In[ ]:


no_subsystem_categorization.str.slice( stop=3 ).value_counts().head(20)


# In[ ]:


no_subsystem_categorization.str.slice( stop=4 ).value_counts().head(20)


# In[ ]:


no_subsystem_categorization.str.slice( stop=5 ).value_counts().head(20)


# In[ ]:


# nothing here
#no_subsystem_categorization.str.slice( stop=6 ).value_counts().head(20)


# In[ ]:


no_subsystem_categorization.str.contains( 'DLD' ).sum()


# #### Pivot out subsystem annotations

# In[ ]:


program_table_df


# #### Map tables to PLAS subsystems

# In[ ]:


table_susbystem_pivot = program_table_df.pivot_table(
    index='table_index',
    columns='subsystem',
    values='leading_space_count', #something guaranteed not to be empty
    aggfunc='count'
).fillna(0).astype(bool).astype(int)


# In[ ]:


table_susbystem_pivot.columns


# In[ ]:


len(table_susbystem_pivot.columns )


# In[ ]:


table_susbystem_pivot = table_susbystem_pivot[ table_subsystem_counts['code'].values ]


# ### SUBSCHEMA analysis

# In[49]:


selection_criteria = ( lines_df['leading_space_count'] == 9 ) & lines_df['line'].str.contains( "SCHEMA" )


# In[50]:


subschema_df = lines_df[ selection_criteria ]


# In[51]:


subschema_df.shape


# In[54]:


pd.set_option( 'display.max_colwidth', 200 )


# In[56]:


p = re.compile( r'^\s+SUBSCHEMA\s+(\S+)\s+OF SCHEMA\s+(\S+)\s+VER' )


# In[59]:


subschema_data_df = subschema_df['line'].str.extract( p )


# In[60]:


subschema_data_df.columns = ['subschema', 'schema' ]


# In[61]:


subschema_data_df['schema'].value_counts()


# In[63]:


subschema_data_df['subschema'].value_counts()


# ## 10's through 12's are data elements

# In[64]:


text_clumps[10][-10:]


# In[65]:


text_clumps[11][-10:]


# In[66]:


text_clumps[12][-10:]


# In[67]:


all_data_elements = [ *text_clumps[10], *text_clumps[11], *text_clumps[12] ]


# In[68]:


len( all_data_elements )


# ## Include data elements from lines with 13 spaces

# In[69]:


len(text_clumps[13])


# In[70]:


text_clumps[13][:20]


# In[71]:


data_elements_13 = [ _ for _ in text_clumps[13] if _[16] == ' ' ]


# In[72]:


len( data_elements_13 )


# In[73]:


data_elements_13


# In[74]:


all_data_elements.extend( data_elements_13 )


# In[75]:


len( all_data_elements )


# ### Get a count of all elements in the base (non-synonym version) of a table
# 
# * FILTER OUT SYNONYMS HERE

# In[76]:


# skip the 9 lines with 13 spaces for now
all_elements = lines_df[ (lines_df['leading_space_count'] >= 10) & (lines_df['leading_space_count'] <= 12) & (lines_df['synonym_index'] == 0) ] 


# In[77]:


lines_df[ 'synonym_index' ].value_counts()


# In[78]:


all_elements.shape


# In[79]:


all_elements.groupby( 'table_index' )['line'].count()


# In[81]:


all_elements[ 'synonym_index' ].value_counts()


# ### Locations
# 
# * [0:15] - declaration step
# * [15:62] - (\s+)(\d+) (\s+)
# * [62:95] - data format
# * [95:] - end

# In[82]:


all_elements.info()


# In[83]:


p = re.compile( r'^\s+(\d+)(\s+)(\d+) (\S+)' )


# In[84]:


p.match( all_data_elements[0] ).groups()


# In[87]:


data_fields = all_elements['line'].str.extract( p )


# In[88]:


data_fields.columns = ['declaration_steps', 'indent', 'indent_number', 'field_name']


# In[94]:


data_fields['indent_space_count'] = data_fields['indent'].transform( len )


# In[89]:


data_fields['data_type'] = all_elements['line'].transform( lambda l: l[62:95].strip() )


# In[90]:


data_fields['field_type'] = all_elements['line'].transform( lambda l: l[95:].strip() )


# In[95]:


data_fields.info()


# In[96]:


data_fields.sample( 10 )


# In[97]:


data_fields[ ['indent_space_count', 'indent_number' ] ].value_counts()


# In[98]:


data_fields[ data_fields[ 'indent_number' ] =='09']


# In[99]:


unique_data_types = set( data_types )


# In[100]:


unique_data_types = sorted( list( unique_data_types ), key=lambda t: ( len(t), t ) )


# In[101]:


Counter( end_types )


# In[102]:


#Path( '2022-10-17_IDMS_COBOL_datatypes.txt' ).write_text( '\n'.join( unique_data_types ) )


# In[103]:


temp = all_elements[ ['table_index', 'synonym_index' ] ]


# In[104]:


temp


# In[105]:


data_fields = pd.concat( (temp, data_fields), axis=1 )


# In[106]:


data_fields


# ## Scrape COMMENTS from lines beginning with 14 spaces (DEFINITION, COMMENT, and PURPOSE)

# In[ ]:


text_clumps[14][:20]


# In[ ]:


comment_lines = lines_df[ lines_df['leading_space_count'] == 14 ]


# In[ ]:


comments = comment_lines.groupby( 'table_index' ).apply( lambda group: " ".join( _[18:] for _ in group['line'].values  ) )


# In[ ]:


comments[2]


# In[ ]:


comments


# ## Merge table subsystem mapping

# In[ ]:


comments.name = 'comments'


# In[ ]:


merged_table_info = merged_table_info.merge( comments, how='left', left_index=True, right_index=True )


# In[ ]:


merged_table_info = merged_table_info.sort_values( ['created_dates', 'table_names', 'table_vers'] )


# In[ ]:


import numpy as np


# In[ ]:


table_susbystem_pivot[ table_susbystem_pivot == 0] = np.nan


# In[ ]:


new_col_names = [ two_letter_code_to_subsystem_desc_map[_] for _ in table_susbystem_pivot.columns ]


# In[ ]:


new_col_names[1] = 'RURAL COMMUNITY FACILITY TRACKING SYSTEM'


# In[ ]:


table_susbystem_pivot.columns = new_col_names


# In[ ]:


merged_table_info = merged_table_info.merge( table_susbystem_pivot, left_index=True, right_index=True, how='left' )


# In[ ]:


merged_table_info.to_excel( '2022-12-15_IDMS_table_descriptions.xlsx' )


# In[ ]:


suffix_df


# In[ ]:


all_table_info = merged_table_info.merge( suffix_df, left_index=True, right_on='table_index' )


# In[ ]:


all_table_info.head()


# In[ ]:


all_table_info['synonym_index'].value_counts()


# In[ ]:


data_fields['synonym_index'].value_counts()


# In[ ]:


all_table_info = all_table_info.drop( columns=['leading_space_count', 'modifies_line', 'line' ] ).sort_index()


# In[ ]:


# all_table_info = all_table_info[ ['table_names', 'synonym_name', 'table_vers', 'created_dates', 'updated_dates',
#        'descriptions', 'comments',  'affix_type', 'affix'] ]


# In[ ]:


all_table_info.sample(10)


# In[ ]:


data_fields


# In[ ]:


data_fields = data_fields.reset_index().rename( columns={'index':'line' } )


# In[ ]:


all_fields_info = data_fields.merge( all_table_info, how='left', on=['table_index', 'synonym_index' ] ).drop( columns=['descriptions', 'comments' ])


# In[ ]:


all_fields_info['field_name_stripped'] = all_fields_info.apply( lambda row: row['field_name'].replace( row['affix'], "" ), axis=1 )


# In[ ]:


len( all_fields_info )


# In[ ]:


all_fields_info.columns


# In[ ]:


all_fields_info['affix'].value_counts().head(20)


# In[ ]:


wanted_columns = ['line', 'table_names', 'table_index', 'table_vers', 'created_dates', 'updated_dates',
       'field_name_stripped', 'data_type', 'indent_number', 'indent_space_count',
       'declaration_step', 'end', 'field_name', ]


# In[ ]:


all_fields_info = all_fields_info[wanted_columns].copy()


# In[ ]:


all_fields_info.columns


# In[ ]:


# RENAME
all_fields_info.columns = [ 'line', 'table_name', 'table_index', 'table_vers', 'table_created_date', 'table_updated_date',
        'field_name',  'data_type', 'indent_number',
       'indent_space_count', 'declaration_step', 'end', 'raw_field_name',]


# In[ ]:


all_fields_info


# # 22's 

# In[ ]:


text_clumps[22][:20]


# # 26's: REDEFINES, OCCURS, VALUE

# In[ ]:


len( text_clumps[26] )


# In[ ]:


all_elements[ 'leading_space_count' ]


# In[ ]:


modifiers_lines_df = lines_df[ lines_df[ 'leading_space_count' ] == 26 ].copy()


# In[ ]:


modifiers_lines_df


# In[ ]:


modifiers_lines_df['modifies_line'].value_counts().value_counts()


# In[ ]:


modifiers_lines_df.loc[58,'line']


# In[ ]:


wanted_cols = ['modifier_type', 'modifier_value' ] 


# In[ ]:


modifiers_lines_df[ wanted_cols ] = modifiers_lines_df['line'].str.extract( r'^\s*(\S+ ?\S*)\s+(\S+.*)$')


# In[ ]:


modifiers_lines_df['modifier_type'] = modifiers_lines_df['modifier_type'].str.strip()


# In[ ]:


modifiers_lines_df = modifiers_lines_df.set_index( 'modifies_line' )[ wanted_cols ]


# In[ ]:


modifiers_lines_df['modifier_type'].value_counts()


# In[ ]:


duplicate_modifiers = modifiers_lines_df[ modifiers_lines_df.index.duplicated(keep=False) ].sort_index()


# In[ ]:


duplicate_counts = duplicate_modifiers.groupby( 'modifies_line' ).apply( lambda group_df: group_df[ "modifier_type" ].value_counts() )


# In[ ]:


pd.set_option( 'display.max_rows', 100 )
#pd.set_option( 'display.max_rows', 100 )


# In[ ]:


#duplicate_counts


# In[ ]:


modifiers_lines_df.info()


# In[ ]:


#modifiers_lines_df


# In[ ]:


pivoted_modifiers = modifiers_lines_df.pivot_table(
    values='modifier_value',
    index='modifies_line',
    columns='modifier_type',
    # Either populate the cell with the single value, or listify multiple values:
    aggfunc=lambda v: list( v ) if len( v ) > 1 else v,
    fill_value=""
)


# In[ ]:


pivoted_modifiers = pivoted_modifiers.reset_index().rename( columns={'modifies_line': 'line' } )


# In[ ]:


pivoted_modifiers.shape


# In[ ]:


all_fields_info


# In[ ]:


all_fields_info = all_fields_info.merge( pivoted_modifiers, on='line', how='left' )


# In[ ]:


all_fields_info.drop(columns=['line']).to_excel( '2022-12-08_PLAS_IDMS_data_structure.xlsx' )

