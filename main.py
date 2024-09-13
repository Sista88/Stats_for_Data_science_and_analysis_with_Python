#!/usr/bin/env python
# coding: utf-8

# # Statistics practical implementation
# 
# 1. Measure of Central Tendency
# 
#     1. Mean
#     2. Median
#     3. Mode

# In[8]:


age = [23, 24, 32, 45, 12, 43, 67, 45, 32, 56, 32, 100]


# In[9]:


import numpy as np
print(np.mean(age))
print(np.median(age))


# In[10]:


import statistics 
print(statistics.mean(age))
print(statistics.median(age))
print(statistics.mode(age))


# In[11]:


import seaborn as sns
sns.boxplot(age)


# ### Five number summary
# 1. minimum value
# 2. 25 percentile
# 3. median (50 percentile)
# 4. 75 percentile
# 5. maximum value

# In[13]:


q1, q3 = np.percentile(age, [25, 75])
print(q1, q3)


# In[16]:


IQR = q3-q1
print("IQR is", IQR)
lower_fense = q1 - 1.5*(IQR)
upper_fense = q3 + 1.5*(IQR)
print("lower fense", lower_fense)
print("upper fense", upper_fense)


# 2. Measure of dispersion
#     1. Variance
#     2. Standard deviation

# In[20]:


statistics.variance(age) #Here it automatically take sample variance


# In[21]:


np.var(age) # Here it is population variance


# In[22]:


statistics.pvariance(age) # statistics lib also directly provides population variance


# In[23]:


import math
sd = math.sqrt(statistics.pvariance(age)) # It gives standard deviation
print(sd)


# In[ ]:




