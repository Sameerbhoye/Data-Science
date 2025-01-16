# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 19:50:57 2024

@author: samir
"""

#Import necessary libraries
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Load the csv File
df=pd.read_csv("E:/Data Science/10-Recommendation_Engine/Entertainment.csv.xls")
df
#step 1. Process the caegory column using TfIDF
tfidf=TfidfVectorizer(stop_words='english') #Remove common stop words 
tfidf_matrix=tfidf.fit_transform(df['Category'])

#step 2: Compute the cosine similarity between titles 
cosine_sim=cosine_similarity(tfidf_matrix, tfidf_matrix)

#step 3: Create a function to reccomend titles based on similarity

def get_recommendations(title, cosine_sim=cosine_sim):
    #Get the index of title that matches the input title
    idx=df[df['Titles']==title].index[0]
    #Get the pairwise similarity scores of all titles with that title 
    sim_scores=list(enumerate(cosine_sim[idx]))
    #sort the title  based on the similaritty scorss in describing 
    sim_scores=sorted(sim_scores, key=lambda x: x[1],reverse=True)
    #get the indeices of the most similar titles
    sim_indices=[i[0]for i in sim_scores[1:6]]
    #return the top 5 most similar titles
    return df['Titles'].iloc[sim_indices]

#test the recommendation system with an example
example_title='Toy Story(1995)'
recommended_titles=get_recommendations(example_title)
#print the recommendations 
print(f"Recommendations for '{example_title}': ")

for title in recommended_titles:
    print(title)

    
    
    















