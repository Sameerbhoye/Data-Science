# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 08:23:01 2024

@author: samir
"""

import pandas as pd
import matplotlib.pyplot as plt 
#
Univ1=pd.read_excel("E:/Data Science/7-Clustering/University_Clustering.xlsx")
a=Univ1.describe()
#we have one column state which really not useful we will drop it 
Univ=Univ1.drop(["State"], axis=1)
#we Know that there is scale diffrerence among the columns
#which we have to remove 
#either by using  normalization or standardization
#whenever there is mixed data apply normalization
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
#Now apply normalization function to Univ dataframe
#for all the rows and columns from 1 until end 
#since 0th column has university name hence 
df_norm=norm_func(Univ.iloc[:,1:])
#you can check the df_norm dataframe which is scaled 
#between values from 0 to 1 
#you can apply describe function to new dataframe 
b=df_norm.describe()
#Before you apply clustering you need to plot dendrogram first 
#Now to create dendrogram we need to measure distance 
#we have to import linkage 
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch
#linkage function given us hierarchical or aglomerative clustering 
#redf the help for linkage
z=linkage(df_norm, method="complete",metric="euclidean")
plt.figure(figsize=(15,8))
plt.title("Hierarchical Clustering dendrogram");
plt.xlabel("Index");
plt.ylabel("Distance")
#
#
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()
#dendroogram
#
#
#It isjust showing number of possible clusters  
from sklearn.cluster import AgglomerativeClustering 
h_complete=AgglomerativeClustering(n_clusters=3, linkage='complete', metric="euclidean").fit(df_norm)
#apply labels to the clusters 
h_complete.labels_
cluster_labels=pd.Series(h_complete.labels_)
#assign this series to univ dataframe  as clumns and name the as culumn as cluster_labels 
Univ['clust']=cluster_labels
#we want relocate the column 7 to 0th position
Univ1=Univ.iloc[:,[7,1,2,3,4,5,6]]
#now check the univ1 dataframe 
Univ1.iloc[:,2:].groupby(Univ.clust).mean()
#from the output cluster 2 has got highest Top 10





























