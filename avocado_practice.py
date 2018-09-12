
# coding: utf-8

# # Pandas practice
# #Plan on importing an avocado data set

# In[5]:


#import pandas as pd 
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


avoprice_data = pd.read_csv("/Users/hunterromano/Desktop/avocado 3.csv")


# In[7]:


#Look at the data
avoprice_data


# In[10]:


#frame the data, give me first five rows
avoprice_data.head()


# In[12]:


#look at types and only first five
avoprice_data [["type"]].head()


# In[20]:


# look at number of data points
avoprice_data ["type"].value_counts()

