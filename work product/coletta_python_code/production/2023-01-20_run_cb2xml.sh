#!/bin/sh
# coding: utf-8

# # Fixing bugs in cobol copybook generation python script
# 
# ## Install Azul Zulu - which works on arm64-based Apple M1 processors
# 
# * [Azul Zulu builds of OpenJDK](https://docs.azul.com/core/zulu-openjdk/install/macos)
# 
# 
# ## Installing CB2XML
# * [CB2XML on github](https://github.com/bmTas/cb2xml)
#     * [download from sourceforge](https://sourceforge.net/projects/cb2xml/files/latest/download)

# In[1]:


neofetch


# In[2]:


which java


# In[3]:


java -version


# In[4]:


file cb2xml/lib/cb2xml.jar


# In[5]:


java -jar cb2xml/lib/cb2xml.jar


# In[6]:


cat ABSDOMN_7_lines.txt


# In[7]:


java -jar cb2xml/lib/cb2xml.jar -cobol ABSDOMN_7_lines.txt -indentXml


# In[39]:


java -jar cb2xml/lib/cb2xml.jar -cobol 2023-02-01_IDMS_Copybooks_FPAC_schemas.txt -indentXml -xml 2023-01-27_Coletta_IDMS_all_scraped_copybooks.xml


# In[27]:


cp 2023-01-27_Coletta_IDMS_all_scraped_copybooks.csv 2023-01-27_IDMS_Copybooks_FARMS_schema_only.csv


# In[29]:


head -100 2023-01-27_IDMS_Copybooks_FARMS_schema_only.csv


# In[ ]:


grep -A 15 "ACCRLINK" IDMS_RECORDS_no_trailing_whitespace.txt


# In[ ]:


ls PLAS.MISSING.CPYBOOKS.cpy/


# In[ ]:


grep -n1 "REDEFINES" PLAS.MISSING.CPYBOOKS.cpy/*


# In[ ]:


grep -n1 "COMP-3" PLAS.MISSING.CPYBOOKS.cpy/*


# In[ ]:




