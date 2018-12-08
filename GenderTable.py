#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
conn = sqlite3.connect('demographics.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Gender')
cur.execute('CREATE TABLE Gender (Zip_Code INTEGER, Number_Surveyed INTEGER, Count_Females INTEGER, Count_males INTEGER)')

conn.close()


# In[2]:


from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import exists
from sqlalchemy import sql, select, join, desc

# Create a sqlite database
engine = create_engine('sqlite:///Gender.sqlite')

metadata=MetaData(engine)

# Create Popular Table
Gender = Table ('Demographics', metadata,
                Column('Zip Code', Integer, primary_key=True),
                Column('Number Surveyed', Integer),
                Column('Number of Males', Integer, autoincrement=True),
                Column('Number of Females', Integer),
                Column('Year', Integer)
               )
metadata.create_all(engine)


# In[8]:





# In[11]:


import sqlite3

# Insert data into database using the sqlite3 module
conn = sqlite3.connect('demographics.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Gender (Zip_Code, Number_Surveyed, Count_Females, Count_Males) VALUES (?, ?, ?, ?)',
    ( 10001, 44, 22, 22 ))
cur.execute('INSERT INTO Gender (Zip_Code, Number_Surveyed, Count_Females, Count_Males) VALUES (?, ?, ?, ?)',
    ( 10002, 35, 19, 16 ))
cur.execute('INSERT INTO Gender (Zip_Code, Number_Surveyed, Count_Females, Count_Males) VALUES (?, ?, ?, ?)',
    ( 10003, 1, 1, 0 ))
cur.execute('INSERT INTO Gender (Zip_Code, Number_Surveyed, Count_Females, Count_Males) VALUES (?, ?, ?, ?)',
    ( 10004, 0, 0, 0 ))
cur.execute('INSERT INTO Gender (Zip_Code, Number_Surveyed, Count_Females, Count_Males) VALUES (?, ?, ?, ?)',
    ( 10005, 2, 2, 0 ))
cur.execute('INSERT INTO Gender (Zip_Code, Number_Surveyed, Count_Females, Count_Males) VALUES (?, ?, ?, ?)',
    ( 10006, 6, 2, 4 ))
cur.execute('INSERT INTO Gender (Zip_Code, Number_Surveyed, Count_Females, Count_Males) VALUES (?, ?, ?, ?)',
    ( 10007, 1, 0, 1 ))
cur.execute('INSERT INTO Gender (Zip_Code, Number_Surveyed, Count_Females, Count_Males) VALUES (?, ?, ?, ?)',
    ( 10009, 2, 0, 2 ))
cur.execute('INSERT INTO Gender (Zip_Code, Number_Surveyed, Count_Females, Count_Males) VALUES (?, ?, ?, ?)',
    ( 10010, 0 , 0, 0 ))

conn.commit()


# In[ ]:




