#!/usr/bin/env python
# coding: utf-8

# In[2]:


with open("E://data/BABAnews.txt", mode = 'r',encoding='UTF-8') as myfile: 
        print(myfile.read())


# In[3]:


myfile.closed


# In[5]:


myfile = open("E://data/BABAnews.txt", mode = 'r',encoding='UTF-8')
text = myfile.read()
myfile.close()
print(text)


# In[14]:


myfile = open("E://data/BABAnews.txt", mode = 'r',encoding='UTF-8')
myfile.read()


# In[15]:


myfile = open("E://data/BABAnews.txt", mode = 'r',encoding='UTF-8')
myfile.readlines()


# In[16]:


with open('E://data/Titanic.csv', 'r') as myfile:
    for line in myfile:
        print(line, end ='')


# In[18]:


file = open('E://data/testfile.txt', 'w') 
file.write('Hello World \n') 
file.write('and this is another line.') 
file.close() 


# In[20]:


pi = 3.141592
fout = open('E://data/math.txt', 'w')
fout.write("Pi's value is ")
fout.write(str(pi))
fout.close()


# In[23]:


import csv
with open('E://data/Titanic.csv') as csvfile:
    titanicReader = csv.reader(csvfile)
    for row in titanicReader:
        print('  '.join(row))


# In[25]:


import pandas as pd
titanicData = pd.read_csv('E://data/Titanic.csv') 
titanicData.head()


# In[ ]:




