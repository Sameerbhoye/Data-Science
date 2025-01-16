# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 08:33:23 2024
'''Crisp MLQ'''

@author: samir
"""

import pandas as pd
#let us import datasets

df=pd.read_csv("E:/Data Science/5-Data_Prep/ethnic diversity.csv.xls")
#let us check datatypes of columns
df.dtypes
#Salaries dataype is float, let's convert it into int
#df1=df.Salaries.astype(int)
df.Salaries=df.Salaries.astype(int)
df.dtypes
#similarly age data type must be float, presently it is int
df.age=df.age.astype(float)
df.dtypes

###################################################
#Identify the duplicates

df_new=pd.read_csv("E:/Data Science/5-Data_Prep/education.csv.xls")
duplicate=df_new.duplicated()
#Output of this function is one column
#if duplicated data is present then True
#if duplicated data is not present then it is False
#Series will be created
duplicate
sum(duplicate)
#output will be 0
#now lets import another dataset
df_new1=pd.read_csv("E:/Data Science/5-Data_Prep/mtcars_dup.csv.xls")
duplicate1=df_new1.duplicated()
duplicate1
sum(duplicate1)
#There atre 3 duplicate records
#row 17 is a duplicate of row 2
#the function drop_duplicates() will drop all duplicate records
df_new2=df_new1.drop_duplicates()
duplicate2=df_new2.duplicated()
duplicate2
sum(duplicate2)

#####################################################
#Trimming
import pandas as pd
import seaborn as sns
df=pd.read_csv("E:/Data Science/5-Data_Prep/ethnic diversity.csv.xls")
#Now let us find outliers in Salaries
sns.boxplot(df.Salaries)
#There are outliers
#Let us check outliers in age column
sns.boxplot(df.age)
IQR=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
IQR
