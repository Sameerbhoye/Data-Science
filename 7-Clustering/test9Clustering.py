# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:15:34 2024

@author: samir
"""

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


df=pd.read_csv("E:/Data Science/7-Clustering/HeightWeight.csv")
df
df.describe()
df.shape
df.head()
twss=[]
#We need to normalize the data 
def df_norm(i):
    normal=((i-i.min())/(i.max()-i.min()))
    return normal
#dnorm.head()


TWSS=[]
k=list(range(2,8))
for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(df_norm)
    
    TWSS.append(kmeans.inertia_)#total sum of square
'''
Kmeans inertia also kowns as sum of square Errors  
(or SSE). calculates the sum of distances of all points within a cluster  from centroid of 
of the point . It is the difference betweeen the obserrved value and predicted value


'''
TWSS
#
plt.plot(k,TWSS,'ro-');
plt.xlabel("No_of_clusters");
plt.xlabel("Total_within_SS")
'''
How to select value of the elbow curve 
when k changes from  2 to 3, then decrease
in twss is higher than 
when k changes from 3 to 4 
when k values changes from 5 to 6 decrease 
'''

model=KMeans(n_clusters=3)
model.fit(df_norm)
model.labels_
mb=pd.Series(model.labels_)
df['clust']=mb
df.head()
df=df.iloc[:,[7,0,1,2,3,4,5,6]]
df
df.iloc[:,2:8].groupby(df.clust).mean()

df.to_csv("kmeans_University.csv",encoding="utf-8")

        
        
        
import pandas as pd


mall=pd.read_csv("E:/Data Science/7-Clustering/Mall_Customers.csv")
mall.head()


def df_norm(i):
    normal=((i-i.min())/(i.max()-i.min()))
    return normal
     
        