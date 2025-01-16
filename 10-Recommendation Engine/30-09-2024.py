# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 08:57:06 2024

@author: Samir
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#load the csv file
file_path = "E:/Data Science/10-Recommendation_Engine/Entertainment.csv.xls"
data=pd.read_csv(file_path)

#Step 1:- Preprocess the 'category' column using TF-TDF
tfidf = TfidfVectorizer(stop_words='english') 
tfidf_matrix = tfidf.fit_transform(data['Category'])

#Step 2:- Compute the cosine similarity between titles
cosine_sim = cosine_similarity(tfidf_matrix,tfidf_matrix)

#Step 3:- Create a function to recommend titles based on similarity 
def get_recommendation(title, cosine_sim=cosine_sim):
    # Get the index of the title that matches the input titles
    idx = data[data['Titles'] == title].index[0]
    
    #Get the  paiirwise similarity scores of all titles with that title
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    #sort the titles 
    sim_scores = sorted(sim_scores, key=lambda x: x[1],reverse=True)
    
    # Get the top 5 most similar titles
    sim_indices = [i[0] for i in sim_scores[1:6]]
    #Exclude the first as it's the title itself
    
    # Return the top 5 most similar titles
    return data['Titles'].iloc[sim_indices]

# test the recommendation system with an example title
example_title = "Toy Story (1995)"
recommended_title = get_recommendation(example_title)

#Print the recommendation
print(f"Recommendation for '{example_title}':")

for title in recommended_title:
    print(title)
    
    
####################################################################################################
'''
01-10-2024
'''

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as  np

file_path = "E:/Data Science/10-Recommendation_Engine/game.csv.xls"
data = pd.read_csv(file_path)

#Step 1 :- Create a user_item_matrix = data.pivot_table(index:userId, columns:game,values:rating)
user_item_matrix = data.pivot_table(index='userId', columns='game',values='rating')
'''
pivot_table: This function reshapes the Dataframe into a matrix where::
    
    Each row represents a user(identified by userId).
    Each column represents a game (identified by game). 
    The values in the matrix represent the ratings that 
    users gave to the games.

'''
# Step 2 :- Fill NaN values
user_item_matrix_filled = user_item_matrix.fillna(0)
'''    

This Line replaces any missing values (NaNs)
in the user-item matrix with 0, 
indicating that the user did not rate that particular game.

'''

# Step 3 :- Compute the cosine similarity between users based on raw ratings 
user_similarity = cosine_similarity(user_item_matrix_filled)

#Convert similarity matrix to a  Datafframe for easy reference 
user_similarity_df = pd.DataFrame(user_similarity, index = user_item_matrix.index, columns=user_item_matrix.index)

# Step 4 : funnction to get game recommmendations for a specific user based on
def get_collaborative_recommendations_for_user(user_id,num_recommendations=5):
    #Get the similarity scores for the input user with all other users
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)
    
    #Get the most similar users
    similar_users=similar_users.drop(user_id)
    
    #select the Top N similar users to limit noise 
    top_similar_users = similar_users.head(50)
    #THis selected top 30 most similar userss to limit nnoise in tthe recommendations
    #Get the ratings 
    weighted_ratings = np.dot(top_similar_users.values, user_item_matrix_filled.loc[top_similar_users.index])
    #np.dot: This computes the dot product between the 
    #similarity scores of the top similar users and
    #their corresponding ratings in the user-item matrix.
    #The result is an array of weighted ratings for each game.
    #Normalize by the sum of similarities
    sum_of_similarities = top_similar_users.sum()
    
    if sum_of_similarities > 0:
        weighted_ratings /= sum_of_similarities
       # the weighted rating are normalized by by diving by the 
       # sum of similarities to avoid biasing towords user with highrt
       
       # Recommend games that the usres hasnt rated yet 
    user_ratings = user_item_matrix_filled.loc[user_id]
    unrated_games = user_ratings[user_ratings==0]
        # indentifies gamesd that the target usee not rated(i.e, rated 0)
        # get the weighted scores for unrated games
    game_recommendations = pd.Series(weighted_ratings, index=user_item_matrix_filled.columns).loc[unrated_games.index]
        #This creates a pandas Series from the weighted ratings 
        #and filters it to include only the unrated games. 
        #Finally, it sorts the recommendations in descending order 
        #and returns the top specified number of recommendations.

        #Return the top num recommendations game recommendations
        
    return game_recommendations.sort_values(ascending=False).head(num_recommendations)
                                         
#Example usage: Get recommendaetions for a user with ID 3
recommended_games = get_collaborative_recommendations_for_user(user_id=3)
      
print("Recommended games for user 3: ")    
print(recommended_games)    
 






























