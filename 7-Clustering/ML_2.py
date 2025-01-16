# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 08:33:02 2024

@author: samir
"""

import pandas as pd 
import numpy as np
import matplotlib.pylab as plt
from sklearn.cluster import KMeans 
#
#
#
#
X=np.random.uniform(0,1,50)
Y=np.random.uniform(0,1,50)
#create a empty dataframe with 
df_xy=pd.DataFrame(columns=["X","Y"])
#assign the values of x and y to these columns 
df_xy.X=X
df_xy.Y=Y
df_xy.plot(x="X",y="Y",kind="scatter")
model1=KMeans(n_clusters=3).fit(df_xy)
'''With the data X and y, apply Kmeans model
generate scatter plot with scale/font=10
camp=plt.cm.coolwarm:cool color combination'''
model1.labels_
df_xy.plot(x="X",y="Y",c=model1.labels_, kind="scatter",s=10,cmap=plt.cm.coolwarm)
######################################

Univ1=pd.read_excel("E:/Data Science/7-Clustering/University_Clustering.xlsx")
Univ1.describe()
Univ=Univ1.drop(["State"],axis=1)
#We know that there is scale differnce among the columns , which  
#
#
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
#Now aply
df_norm=norm_func(Univ.iloc[:,1:])
'''
what will be ideal cluster number, will it be 1,2 or 3
'''
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
Univ['clust']=mb
Univ.head()
Univ=Univ.iloc[:,[7,0,1,2,3,4,5,6]]
Univ
Univ.iloc[:,2:8].groupby(Univ.clust).mean()

Univ.to_csv("kmeans_University.csv",encoding="utf-8")
import os
os.getcwd()


#
#
#
#
#
#
#

import  pandas as pd 




