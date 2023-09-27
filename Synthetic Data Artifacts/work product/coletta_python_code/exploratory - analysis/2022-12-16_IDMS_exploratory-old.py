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


#ls


# In[6]:


pd.set_option( 'display.max_rows', 200 )


# In[7]:


#subsystems = pd.read_excel( "PLAS Subsystem Schema -Revised.xlsx", index_col=0)


# # PLAS subsystems names

# In[8]:


subsystems = pd.read_excel( "PLAS Subsystem Schema -Revised.xlsx", index_col=0, sheet_name=1)


# In[9]:


wanted_columns = ['Program\nSchema', 'System Name' ]


# In[10]:


drop_these = set( subsystems.columns ) - set( wanted_columns )


# In[11]:


subsystems = subsystems.drop( columns=drop_these )


# In[12]:


subsystems.columns = ['code', 'plas_subsystem' ]


# In[13]:


subsystems[ subsystems['code'] == 'BD' ]


# In[14]:


subsystems = subsystems.drop( index = 122 )


# ## Systems without a code

# In[15]:


no_code = subsystems[ subsystems['code'] == '**' ]


# In[16]:


no_code


# In[17]:


subsystems = subsystems.drop( index = no_code.index )


# In[18]:


subsystems.shape


# In[19]:


subsystems = subsystems.dropna( subset=['code'] )


# In[20]:


subsystems.shape


# In[21]:


subsystems.sort_values( 'code' )


# In[22]:


two_letter_code_to_subsystem_desc_map = dict( subsystems.values )


# In[23]:


#!cp /Users/ccoletta/Library/CloudStorage/Box-Box/GSA\ USDA\ -\ CONTRACTOR\ ACCESS/PLAS_CODE_AND_DOCUMENTAION/file_lengths.txt .


# # Analysis of COBOL programs obtained in discovery (line counts for each file)

# In[24]:


files = pd.read_csv( 'file_lengths.txt', header=None  )


# In[25]:


files.columns = ['raw_line']


# In[26]:


files = files['raw_line'].str.split(expand=True)


# In[27]:


files.columns = ['line_count', 'file_path']


# In[28]:


files['n_slashes'] = files['file_path'].str.count('/')


# In[29]:


files['n_slashes'].value_counts()


# In[30]:


#files['file_path'].str.contains( 'PLAS_documentation' ).value_counts()
#files = files[ ~files['file_path'].str.contains( 'PLAS_documentation' ) ].copy()
#files = files[ ~files['file_path'].str.contains( 'archive_of_archives' ) ].copy()
#files = files[ files['n_slashes'] == 2].copy()


# In[31]:


path_parts = files['file_path'].str.split( '/', expand=True )


# In[32]:


files[ ['file_dir', 'file_name' ] ] = path_parts[ [1,2] ]


# In[33]:


files


# In[34]:


files = files[ ['line_count', 'file_dir', 'file_name' ] ].copy()


# In[35]:


files = files.reset_index(drop=True)


# In[36]:


files['file_name_len'] = files['file_name'].apply( len ) 


# In[37]:


files['file_name_len'].value_counts()


# In[38]:


#tuple( two_letter_code_to_subsystem_desc_map.keys() )


# In[39]:


files.shape


# In[40]:


files = files.sort_values( ['file_dir', 'file_name' ] )


# In[41]:


files


# In[42]:


file_counts = files['file_name'].value_counts()


# In[43]:


dupes = set( file_counts[ file_counts != 1 ].index )


# In[44]:


multiple_places = files[ files['file_name'].isin( dupes ) ].groupby( 'file_name' )[ 'file_dir' ].agg( set )


# In[45]:


multiple_places['ABBM08']


# ## Match COBOL filenames to their PLAS subsystem via two-letter naming convention

# In[46]:


valid_codes = tuple( sorted( list( two_letter_code_to_subsystem_desc_map.keys() ) ) )


# In[47]:


files['categorized'] = files['file_name'].str.startswith( valid_codes )


# In[48]:


files['categorized'].value_counts()


# In[49]:


files


# In[50]:


from collections import Counter


# In[51]:


categorized = files[ files['categorized'] ]


# In[52]:


Counter( [ _[:2] for _ in categorized['file_name'].values ] ).most_common(n=30)


# In[53]:


Counter( [ _[:3] for _ in categorized['file_name'].values ] ).most_common(n=30)


# In[54]:


Counter( [ _[:4] for _ in categorized['file_name'].values ] ).most_common(n=30)


# In[55]:


Counter( [ _[:5] for _ in categorized['file_name'].values ] ).most_common(n=30)


# In[56]:


uncategorized = files[ ~files['categorized'] ]


# In[57]:


uncategorized.shape


# In[58]:


Counter( [ _[:1] for _ in uncategorized['file_name'].values ] ).most_common()


# In[59]:


Counter( [ _[:2] for _ in uncategorized['file_name'].values ] ).most_common( 30 )


# In[60]:


Counter( [ _[:3] for _ in uncategorized['file_name'].values ] ).most_common( 30 )


# In[61]:


Counter( [ _[:4] for _ in uncategorized['file_name'].values ] ).most_common( 30 )


# In[62]:


Counter( [ _[:5] for _ in uncategorized['file_name'].values ] ).most_common( 30 )


# In[63]:


Counter( [ _[:6] for _ in uncategorized['file_name'].values ] ).most_common( 30 )


# ## Line count analysis

# In[64]:


files['file_dir'].value_counts()


# In[65]:


files['line_count'] = files['line_count'].astype( int )


# In[66]:


files.info()


# In[67]:


line_count_analysis = files.groupby( 'file_dir' )['line_count'].describe().round().astype( int )


# In[68]:


line_count_analysis.sort_values( '50%', ascending=False )


# # Analysis/transformation of IDMS data dictionary file "IDMS_RECORDS_cpy.txt"

# ## Initial cleaning

# In[69]:


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


# In[70]:


out = Path( "2022-10-14_Stripped_IDMS_RECORDS.txt" )


# In[71]:


#out.write_text( removed_headers )


# In[72]:


# reload after some hand-editing
removed_headers = out.read_text()


# In[73]:


len( removed_headers )


# In[74]:


lines = removed_headers.split( '\n' )


# In[75]:


len( lines )


# In[76]:


p = re.compile( r'^\s+' )


# In[77]:


p.findall( lines[0] )


# In[78]:


[ i for i, _ in enumerate( lines ) if len( p.findall( _ ) ) == 0 ]


# In[79]:


lines = [ _ for _ in lines if _ != "" ]


# In[80]:


len( lines )


# In[81]:


[ i for i, _ in enumerate( lines ) if len( p.findall( _ ) ) == 0 ]


# In[82]:


leading_space_count = [ len( p.findall( _ )[0] ) for _ in lines if len( p.findall( _ ) ) > 0 ]


# In[83]:


Counter( leading_space_count )


# ## Create grouping variables based on position

# In[84]:


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


# In[85]:


#table_indices


# In[86]:


len( leading_space_count ) == len( lines )


# In[87]:


import pandas as pd


# In[88]:


lines_df = pd.DataFrame( dict(
    leading_space_count = leading_space_count,
    table_index = table_indices,
    synonym_index = synonym_indices,
    modifies_line = modifier_target_lines,
    line = lines ))


# In[89]:


lines_df.info()


# In[90]:


lines_df[ lines_df[ 'modifies_line' ] > 0]


# In[91]:


lines_df[ 'modifies_line' ].value_counts().value_counts()


# In[92]:


lines_df[ lines_df['leading_space_count'] == 1 ]


# In[93]:


text_clumps = lines_df.groupby( 'leading_space_count' ).apply( lambda group: group['line'].to_list() )


# In[94]:


text_clumps.info()


# In[95]:


[ len( _ ) for _ in text_clumps ]


# In[96]:


lines_df['synonym_index'].value_counts()


# ## TABLE NAMES

# In[97]:


text_clumps[1][:20]


# In[98]:


Counter( [ len(_) for _ in text_clumps[1] ] )


# In[99]:


p = re.compile( r'\s(\S+)\s+VER\s+(\d+)' )


# In[100]:


table_info_list = [ p.match( _ ).groups(1) for _ in text_clumps[1] ]


# In[101]:


len( table_info_list )


# In[102]:


table_info_list[:10]


# In[103]:


table_names, table_vers = zip(*table_info_list )


# In[104]:


created_dates = pd.to_datetime( [ _[101:109] for _ in text_clumps[1] ] )


# In[105]:


len( created_dates )


# In[106]:


updated_dates = pd.to_datetime( [ _[92:100] for _ in text_clumps[1] ], errors='coerce' )


# In[107]:


updated_dates


# In[108]:


table_info = pd.DataFrame( data=dict(
    table_names=table_names,
    table_vers=table_vers,
    created_dates=created_dates,
    updated_dates= updated_dates
))


# In[109]:


table_info['created_dates'] = table_info['created_dates'].dt.date
table_info['updated_dates'] = table_info['updated_dates'].dt.date


# In[110]:


table_info.info()


# In[111]:


table_info.head(20)


# ## Lines beginning with 5 spaces contain table metadata

# In[112]:


text_clumps[5][:20]


# In[113]:


p = re.compile( r'     (\S+)' )


# In[114]:


Counter( [ p.match( _ ).groups(1)[0] for _ in text_clumps[5] ] )


# ### Pull DESCRIPTION one-liners

# In[115]:


p = re.compile( r'^ (\S+)\s+VER\s+(\d+).*?DESCRIPTION\s+(.*?)$', flags=re.DOTALL | re.MULTILINE ) 


# In[116]:


desc_table_names, desc_table_vers, desc_descs = zip( *p.findall( removed_headers ) )


# In[117]:


len( desc_table_names )


# In[118]:


len( desc_table_vers )


# In[119]:


len( desc_table_names) 


# In[120]:


descs = pd.DataFrame( dict(
    table_names = desc_table_names,
    table_vers = desc_table_vers,
    descriptions = desc_descs ))


# In[121]:


table_info.shape


# In[122]:


descs.shape


# In[123]:


merged_table_info = table_info.merge( descs, on=['table_names', "table_vers"], how='left' )


# In[124]:


merged_table_info


# ### Pull synonym table names, prefixes and suffixes

# In[125]:


suffix_df = lines_df[ lines_df['leading_space_count'] == 5 ]


# In[126]:


suffix_df.shape


# In[127]:


suffix_df = suffix_df[ suffix_df['line'].str.startswith( '     RECORD' ) ]


# In[128]:


suffix_df = suffix_df.copy()


# In[129]:


suffix_df.info()


# In[130]:


name_start_pos = 26
name_end_pos = 67
affix_type_start_pos = 80
affix_type_end_pos = 86
affix_start_pos = 87


# In[131]:


suffix_df['synonym_name'] = [ _[26:67].strip() for _ in suffix_df['line'].values ]


# In[132]:


suffix_df['affix_type'] = [ _[80:86] if len(_) > 80 else "" for _ in suffix_df['line'].values  ]


# In[133]:


suffix_df['affix'] = [ _[87:] if len(_) > 80 else "" for _ in suffix_df['line'].values  ]


# #### There exists 4126 total synonyms

# In[134]:


suffix_df.shape


# In[135]:


suffix_df.head(40)


# In[136]:


suffix_df.to_csv( '2023-01-10_IDMS_table_affixes.csv' )


# In[137]:


# temp = list( suffix_df['line'] )

# temp[:5]

# temp[0][67:76]

# temp[0].index("VER")

# #p = re.compile( r' ' )

# #suffix_df.groupby( 'table_index' ).apply( , axis=1, result_type='expand' )


# ## Lines beginning with 9 spaces indicate "COPIED IN PROGRAM", "FILE", AND "SUBSCHEMA"

# In[141]:


#text_clumps[9][-200:]
#text_clumps[9][-20:]


# In[142]:


p = re.compile( r'\s+(\S+)' )


# In[143]:


Counter( [ p.match( _ ).groups(1)[0] for _ in text_clumps[9] if p.match( _ ) ] )


# In[144]:


#sorted( [ _ for _ in text_clumps[9] if "FILE" in _ ] )


# In[145]:


#[ _ for _ in text_clumps[9] if "LANGUAGE" in _ ]


# In[146]:


#[ _ for _ in text_clumps[9] if "SUBSCHEMA" in _ ]


# In[147]:


#[ _ for _ in text_clumps[9] if "COPIED" in _ ]


# In[148]:


lines_df.info()


# In[149]:


selection_criteria = ( lines_df['leading_space_count'] == 9 ) & lines_df['line'].str.contains( "COPIED" )


# In[150]:


program_table_df = lines_df.loc[ selection_criteria, 'line' ].str.extract( r'(\S+)\s+VER\s+(\d+)$' )


# In[151]:


program_table_df.columns = ['copied_in_program', 'copied_in_program_ver']


# In[152]:


program_table_df


# In[153]:


program_table_df = lines_df.merge( program_table_df, left_index=True, right_index=True, how='right' )


# In[154]:


program_table_df


# # Thirty most popular programs cited in "CALLED IN PROGRAM" statements

# In[155]:


program_table_df['copied_in_program'].value_counts().head(30)


# In[156]:


def GetCode( prog_name ):
    for code in valid_codes:
        if prog_name.startswith( code ):
            return code
    return None


# In[157]:


program_table_df['subsystem'] = program_table_df['copied_in_program'].apply( GetCode )


# ## Twenty most popular subsystems cited in "CALLED IN PROGRAM" statements
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

# In[158]:


subsystem_counts = program_table_df['subsystem'].value_counts().to_frame()


# In[159]:


subsystem_counts = subsystem_counts.reset_index()
subsystem_counts.columns = ['code', 'subsystem_table_count' ]


# In[160]:


table_subsystem_counts = subsystem_counts.merge( subsystems )


# In[161]:


table_subsystem_counts


# In[162]:


program_table_df


# In[163]:


table_to_program_map = program_table_df.groupby( 'table_index' )['copied_in_program'].agg( lambda x: sorted( list( set( x ) ) ) )


# In[164]:


table_to_program_map.name = 'program_list'


# In[165]:


table_to_program_map


# In[166]:


per_table_program_count = table_to_program_map.apply( len )


# In[167]:


per_table_program_count.name = 'per_table_program_count'


# In[168]:


table_to_program_map = pd.concat( ( table_to_program_map, per_table_program_count ), axis=1 )


# # Twenty tables most CALLED IN PROGRAM
# 
# Big winner: table 220

# In[169]:


table_to_program_map.sort_values( "per_table_program_count", ascending=False ).head( 20 )


# In[170]:


table_to_subsystem_map = program_table_df.dropna( subset=['subsystem'] ).groupby( 'table_index' )['subsystem'].agg( lambda x: sorted( list( set(x) ) ) )


# In[171]:


table_to_subsystem_map


# In[172]:


per_table_subsystem_count = table_to_subsystem_map.apply( len )


# In[173]:


per_table_subsystem_count.name = "per_table_subsystem_count"


# In[174]:


table_to_subsystem_map = pd.concat( ( table_to_subsystem_map, per_table_subsystem_count ), axis=1 )


# # Twenty most cross-functional tables
# 
# Winners:
# * 2067
# * 220
# * 743
# * 771

# In[175]:


table_to_subsystem_map.sort_values("per_table_subsystem_count", ascending=False).head(20)


# # Any letter code patterns in the for the programs without subsystems?
# 
# Important patterns:
# 
# * IMD* - 5162
# * S?DLD* - 14149
# * BGD* - 753

# In[176]:


no_subsystem_categorization = program_table_df.loc[ program_table_df['subsystem'].isna(), 'copied_in_program' ]


# In[177]:


no_subsystem_categorization.str.slice( stop=1 ).value_counts().head(20)


# In[178]:


no_subsystem_categorization.str.slice( stop=2 ).value_counts().head(20)


# In[179]:


no_subsystem_categorization.str.slice( stop=3 ).value_counts().head(20)


# In[180]:


no_subsystem_categorization.str.slice( stop=4 ).value_counts().head(20)


# In[181]:


no_subsystem_categorization.str.slice( stop=5 ).value_counts().head(20)


# In[182]:


# nothing here
#no_subsystem_categorization.str.slice( stop=6 ).value_counts().head(20)


# In[183]:


no_subsystem_categorization.str.contains( 'DLD' ).sum()


# # Pivot out subsystem annotations

# In[184]:


program_table_df


# # Map tables to PLAS subsystems

# In[185]:


table_susbystem_pivot = program_table_df.pivot_table(
    index='table_index',
    columns='subsystem',
    values='leading_space_count', #something guaranteed not to be empty
    aggfunc='count'
).fillna(0).astype(bool).astype(int)


# In[186]:


table_susbystem_pivot.columns


# In[187]:


len(table_susbystem_pivot.columns )


# In[188]:


table_susbystem_pivot = table_susbystem_pivot[ table_subsystem_counts['code'].values ]


# # 10's through 12's are data elements

# In[189]:


text_clumps[10][-10:]


# In[190]:


text_clumps[11][-10:]


# In[191]:


text_clumps[12][-10:]


# In[192]:


all_data_elements = [ *text_clumps[10], *text_clumps[11], *text_clumps[12] ]


# In[193]:


len( all_data_elements )


# ## Get a count of all elements in the base (non-synonym version) of a table
# 
# * FILTER OUT SYNONYMS HERE

# In[194]:


all_elements = lines_df[ (lines_df['leading_space_count'] >= 10) & (lines_df['leading_space_count'] <= 12) & (lines_df['synonym_index'] == 0) ] 


# In[195]:


lines_df[ 'synonym_index' ].value_counts()


# In[196]:


all_elements.shape


# In[197]:


all_elements.groupby( 'table_index' )['line'].count()


# In[300]:


dict( _.strip().split( ': ' ) for _ in css.split( ';' ) if _ )


# In[198]:


all_elements[ 'synonym_index' ].value_counts()


# ## Scrape data elements from lines with 13 spaces

# In[199]:


len(text_clumps[13])


# In[200]:


text_clumps[13][:20]


# In[201]:


data_elements_13 = [ _ for _ in text_clumps[13] if _[16] == ' ' ]


# In[202]:


len( data_elements_13 )


# In[203]:


data_elements_13


# In[204]:


all_data_elements.extend( data_elements_13 )


# In[205]:


len( all_data_elements )


# ### Locations
# 
# * [0:15] - declaration step
# * [15:62] - (\s+)(\d+) (\s+)
# * [62:95] - data format
# * [95:] - end

# In[206]:


all_elements.info()


# In[207]:


p = re.compile( r'^\s+(\d+)(\s+)(\d+) (\S+)' )#\s+(\S+)?\s+(\S)$' )
#p = re.compile( r'^\s+(\d+)\s+(\d+) (\S+)\s+(\S+)?\s+(\S)$' )


# In[208]:


p.match( all_data_elements[0] ).groups()


# In[209]:


declaration_steps, indent, indent_number, field_name  = zip( *all_elements['line'].transform( lambda l: p.match( l ).groups() ).values )


# In[210]:


data_types = all_elements['line'].transform( lambda l: l[62:95].strip() )


# In[211]:


# not sure to what to call the "DISPLAY" etc that brings up the rear of these data field lines
end_types = all_elements['line'].transform( lambda l: l[95:].strip() )


# In[212]:


len( data_types )


# In[213]:


len( indent )


# In[214]:


indent = [ len(_) for _ in indent ]


# In[215]:


data_fields = pd.DataFrame(
    data = dict(
        declaration_step = declaration_steps,
        indent_space_count = indent,
        indent_number = indent_number,
        field_name = field_name,
        data_type = data_types,
        end = end_types
    ),
    index = all_elements.index
)


# In[216]:


data_fields.sample( 10 )


# In[217]:


data_fields[ ['indent_space_count', 'indent_number' ] ].value_counts()


# In[218]:


data_fields[ data_fields[ 'indent_number' ] =='09']


# In[219]:


unique_data_types = set( data_types )


# In[220]:


unique_data_types = sorted( list( unique_data_types ), key=lambda t: ( len(t), t ) )


# In[221]:


Counter( end_types )


# In[222]:


#Path( '2022-10-17_IDMS_COBOL_datatypes.txt' ).write_text( '\n'.join( unique_data_types ) )


# In[223]:


temp = all_elements[ ['table_index', 'synonym_index' ] ]


# In[224]:


temp


# In[225]:


data_fields = pd.concat( (temp, data_fields), axis=1 )


# In[226]:


data_fields


# ## Scrape COMMENTS from lines beginning with 14 spaces (DEFINITION, COMMENT, and PURPOSE)

# In[227]:


text_clumps[14][:20]


# In[228]:


comment_lines = lines_df[ lines_df['leading_space_count'] == 14 ]


# In[229]:


comments = comment_lines.groupby( 'table_index' ).apply( lambda group: " ".join( _[18:] for _ in group['line'].values  ) )


# In[230]:


comments[2]


# In[231]:


comments


# ## Merge table subsystem mapping

# In[232]:


comments.name = 'comments'


# In[233]:


merged_table_info = merged_table_info.merge( comments, how='left', left_index=True, right_index=True )


# In[234]:


merged_table_info = merged_table_info.sort_values( ['created_dates', 'table_names', 'table_vers'] )


# In[235]:


import numpy as np


# In[236]:


table_susbystem_pivot[ table_susbystem_pivot == 0] = np.nan


# In[237]:


new_col_names = [ two_letter_code_to_subsystem_desc_map[_] for _ in table_susbystem_pivot.columns ]


# In[238]:


new_col_names[1] = 'RURAL COMMUNITY FACILITY TRACKING SYSTEM'


# In[239]:


table_susbystem_pivot.columns = new_col_names


# In[240]:


merged_table_info = merged_table_info.merge( table_susbystem_pivot, left_index=True, right_index=True, how='left' )


# In[241]:


merged_table_info.to_excel( '2022-12-15_IDMS_table_descriptions.xlsx' )


# In[242]:


suffix_df


# In[243]:


all_table_info = merged_table_info.merge( suffix_df, left_index=True, right_on='table_index' )


# In[244]:


all_table_info.head()


# In[245]:


all_table_info['synonym_index'].value_counts()


# In[246]:


data_fields['synonym_index'].value_counts()


# In[247]:


all_table_info = all_table_info.drop( columns=['leading_space_count', 'modifies_line', 'line' ] ).sort_index()


# In[248]:


# all_table_info = all_table_info[ ['table_names', 'synonym_name', 'table_vers', 'created_dates', 'updated_dates',
#        'descriptions', 'comments',  'affix_type', 'affix'] ]


# In[249]:


all_table_info.sample(10)


# In[250]:


data_fields


# In[251]:


data_fields = data_fields.reset_index().rename( columns={'index':'line' } )


# In[252]:


all_fields_info = data_fields.merge( all_table_info, how='left', on=['table_index', 'synonym_index' ] ).drop( columns=['descriptions', 'comments' ])


# In[253]:


all_fields_info['field_name_stripped'] = all_fields_info.apply( lambda row: row['field_name'].replace( row['affix'], "" ), axis=1 )


# In[254]:


len( all_fields_info )


# In[255]:


all_fields_info.columns


# In[256]:


all_fields_info['affix'].value_counts().head(20)


# In[257]:


wanted_columns = ['line', 'table_names', 'table_index', 'table_vers', 'created_dates', 'updated_dates',
       'field_name_stripped', 'data_type', 'indent_number', 'indent_space_count',
       'declaration_step', 'end', 'field_name', ]


# In[258]:


all_fields_info = all_fields_info[wanted_columns].copy()


# In[259]:


all_fields_info.columns


# In[260]:


# RENAME
all_fields_info.columns = [ 'line', 'table_name', 'table_index', 'table_vers', 'table_created_date', 'table_updated_date',
        'field_name',  'data_type', 'indent_number',
       'indent_space_count', 'declaration_step', 'end', 'raw_field_name',]


# In[261]:


all_fields_info


# # 22's 

# In[262]:


text_clumps[22][:20]


# # 26's: REDEFINES, OCCURS, VALUE

# In[263]:


len( text_clumps[26] )


# In[264]:


all_elements[ 'leading_space_count' ]


# In[265]:


modifiers_lines_df = lines_df[ lines_df[ 'leading_space_count' ] == 26 ].copy()


# In[266]:


modifiers_lines_df


# In[267]:


modifiers_lines_df['modifies_line'].value_counts().value_counts()


# In[268]:


modifiers_lines_df.loc[58,'line']


# In[269]:


wanted_cols = ['modifier_type', 'modifier_value' ] 


# In[270]:


modifiers_lines_df[ wanted_cols ] = modifiers_lines_df['line'].str.extract( r'^\s*(\S+ ?\S*)\s+(\S+.*)$')


# In[271]:


modifiers_lines_df['modifier_type'] = modifiers_lines_df['modifier_type'].str.strip()


# In[272]:


modifiers_lines_df = modifiers_lines_df.set_index( 'modifies_line' )[ wanted_cols ]


# In[273]:


modifiers_lines_df['modifier_type'].value_counts()


# In[274]:


duplicate_modifiers = modifiers_lines_df[ modifiers_lines_df.index.duplicated(keep=False) ].sort_index()


# In[275]:


duplicate_counts = duplicate_modifiers.groupby( 'modifies_line' ).apply( lambda group_df: group_df[ "modifier_type" ].value_counts() )


# In[276]:


pd.set_option( 'display.max_rows', 100 )
#pd.set_option( 'display.max_rows', 100 )


# In[277]:


#duplicate_counts


# In[278]:


modifiers_lines_df.info()


# In[279]:


#modifiers_lines_df


# In[280]:


pivoted_modifiers = modifiers_lines_df.pivot_table(
    values='modifier_value',
    index='modifies_line',
    columns='modifier_type',
    # Either populate the cell with the single value, or listify multiple values:
    aggfunc=lambda v: list( v ) if len( v ) > 1 else v,
    fill_value=""
)


# In[281]:


pivoted_modifiers = pivoted_modifiers.reset_index().rename( columns={'modifies_line': 'line' } )


# In[282]:


pivoted_modifiers.shape


# In[283]:


all_fields_info


# In[284]:


all_fields_info = all_fields_info.merge( pivoted_modifiers, on='line', how='left' )


# In[285]:


all_fields_info.drop(columns=['line']).to_excel( '2022-12-08_PLAS_IDMS_data_structure.xlsx' )

