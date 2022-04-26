# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 18:19:44 2022

@author: dasma
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:58:59 2021
@author: Admin
"""
#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('F:/WORK/pyWork/AnalyticsEdge_Python/pyData/IIT-B.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('F:/WORK/pyWork/AnalyticsEdge_Python/pyData/User_Data.xlsx')

df1 = pandas.read_excel('User_Data.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('IIT-B.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
