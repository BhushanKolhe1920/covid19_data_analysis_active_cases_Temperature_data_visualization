#!/usr/bin/env python
# coding: utf-8

# In[32]:


# Importing all necessary Libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd


# In[33]:


# Reading Excel file data We can even use comma seperated values files.
df1 = pd.read_excel(r"C:\Users\User\Desktop\Data Science\Dataset\Dataset_Actual\Covid_actual_case_temperature.xlsx")


# In[34]:


#Checking whether file is imported or not

df1


# In[35]:


df1.columns


# In[36]:


df1.head()


# In[37]:


df1['Maharashtra']


# In[38]:


# Seaborn library use for scatterplot 
plt.figure(figsize=(10,5))
plt.xticks(rotation=90)
plt.scatter(df1['Month-Year'],df1['Maharashtra'],c='blue')


# In[39]:


plt.xticks(rotation=90)
plt.yticks()

plt.plot(df1['Month-Year'],df1['Maharashtra'],label='MH')
plt.plot(df1['Month-Year'],df1['Punjab'],label='PJ')
plt.plot(df1['Month-Year'],df1['Kerala'],label='KL')
plt.plot(df1['Month-Year'],df1['West Bengal'],label='WB')

plt.xlabel("Month-Year")
plt.ylabel("Active cases")

plt.legend()


# In[40]:


# User based Data Visualization
print("Select from mentioned state : ")
print("1.Maharashtra")
print("2.Kerala")
print("3.West Bengal")
print("4.Punjab")
graph_num=1
for i in range(1,5):
    val = int(input())

   

    if(val==1):
        state = "Maharashtra"
    elif val==2:
        state = "Kerala"
    elif val==3:
        state = "West Bengal"
    elif val==4:
        state = "Punjab"
    else:
        print("Wrong Input")
    if(val>=1 and val<=4):
        plt.subplot(1,4,graph_num)
        graph_num=graph_num+1;
        plt.xticks(rotation=90)
        plt.yticks()
        plt.plot(df1['Month-Year'],df1[state],label=state)
        continue
    
    
    
    else:
        print("---------------------------------------------------------------------------------------------------")
    


# In[41]:


# Rise in Temperature __________________Analysis____________________________________________________________________

print("---------------------------------------------:Temperature data Analysis :--------------------------------------------- ")


# In[42]:


df1


# In[43]:


plt.xticks(rotation=90)

plt.plot(df1['Month-Year'],df1['MH-TEMP'],label='MH')
plt.plot(df1['Month-Year'],df1['WB-TEMP'],label='WB')
plt.plot(df1['Month-Year'],df1['K-TEMP'],label='KL')
plt.plot(df1['Month-Year'],df1['PJ-TEMP'],label='PJ')

plt.xlabel("Year-Month")
plt.ylabel("Temperature in deg. celcius")
plt.legend()


# In[44]:


# Active Covid cases Overall graph
print("-------------------------------------------Active covid cases-----------------------------------------------------------------")


# In[45]:


plt.xticks(rotation=90)

plt.plot(df1['Month-Year'],df1['Maharashtra'],label='MH')
plt.plot(df1['Month-Year'],df1['Kerala'],label='KL')
plt.plot(df1['Month-Year'],df1['Punjab'],label='PJ')
plt.plot(df1['Month-Year'],df1['West Bengal'],label='WB')

plt.legend()
plt.xlabel("Year-Month")
plt.ylabel("Active covid cases")


# In[46]:


# Analysis of side by side Data for conclusion extracting
# Active covid cases
plt.subplot(1,2,1)

plt.xticks(rotation=90)

plt.plot(df1['Month-Year'],df1['Maharashtra'],label='MH')
plt.plot(df1['Month-Year'],df1['Kerala'],label='KL')
plt.plot(df1['Month-Year'],df1['Punjab'],label='PJ')
plt.plot(df1['Month-Year'],df1['West Bengal'],label='WB')

plt.legend()
plt.xlabel("Year-Month")
plt.ylabel("Active covid cases")

# Temperature data

plt.subplot(1,2,2)
plt.xticks(rotation=90)

plt.plot(df1['Month-Year'],df1['MH-TEMP'],label='MH')
plt.plot(df1['Month-Year'],df1['WB-TEMP'],label='WB')
plt.plot(df1['Month-Year'],df1['K-TEMP'],label='KL')
plt.plot(df1['Month-Year'],df1['PJ-TEMP'],label='PJ')

plt.xlabel("Year-Month")
plt.ylabel("Temperature in deg. celcius")
plt.legend()


# In[47]:


# Here we can see some conclusion like

# 1. In Maharashtra region, decrease in covid cases and decrease in temperature  Both are parallel
# 2. In Kerala region, Decrease in covid cases and at  same time we can see rise in temperature
# 3. In Punjab region, we can see two to three spikes where temperature is increasing and covid cases are decreasing.
# 4. In West Bengal region , we can see fall in temperature but spike in covid cases.

# Hence rise and fall in temperature is sometime related to active cases increment. But it is not linear as we can see in above graphs.
# From above data we can conclude that temperature cannont be major factor for incrase or decrease in covid cases.
# However from biological study, temperature of human body is related to covid test.


# In[ ]:




