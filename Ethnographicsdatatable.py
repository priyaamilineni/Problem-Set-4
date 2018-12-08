#!/usr/bin/env python
# coding: utf-8

# In[17]:


import sqlite3
conn = sqlite3.connect('demographics.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Ethnic')
cur.execute('CREATE TABLE Ethnic (Zip_Code INTEGER, Number_Surveyed INTEGER, Pacific_Islander INTEGER, White INTEGER, Hispanic_Latino INTEGER, American_Indian INTEGER, Black INTEGER)')

conn.close()


# In[22]:


from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import exists
from sqlalchemy import sql, select, join, desc

# Create a sqlite database
engine = create_engine('sqlite:///Gender.sqlite')

metadata=MetaData(engine)

# Create Popular Table
Gender = Table ('Ethnic', metadata,
                Column('Zip Code', Integer),
                Column('Number Surveyed', Integer, primary_key=True),
                Column('Asian', Integer),
                Column('White', Integer, autoincrement=True),
                Column('Hispanic Latino', Integer),
                Column('American Indian', Integer),
                Column('Black', Integer),
                )
metadata.create_all(engine)


# In[21]:


import sqlite3

# Insert data into database using the sqlite3 module
conn = sqlite3.connect('demographics.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Ethnic (Zip_Code, Number_Surveyed, Pacific_Islander, White, Hispanic_Latino, American_Indian, Black) VALUES (?,?,?,?,?,?,?)',
    ( 10001, 1, 1, 16, 0, 21, 0))


conn.commit()


# In[ ]:




