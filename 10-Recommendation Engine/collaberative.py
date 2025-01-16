# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:34:12 2024

@author: samir
"""

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
file_path="E:/Data Science/10-Recommendation_Engine/game.csv.xls"
data=pd.read_csv(file_path)

#step1: create a user item matrix(rows: users columns='game',values='rating' )
user_item_matrix=data.pivot_table(index='userId', columns='game',values='rating')

'''  
  pivot_table: This function reshapes the DataFrame into a matrix where:

      Each row represents a user (identified by userId).
      Each column represents a game (identified by game). 
      The values in the matrix represent the ratings that 
      users gave to the games.

'''

#step2: Fill the values with 0 (assuming no rating means the game has not been rated   )
user_item_matrix_filled=user_item_matrix.fillna(0)
'''
This Line replaces any missing values (NaNs) 
in the user-item matrix with 8, indicating that 
the user did not rate that particular game.

'''
#step3:Compute the cosine similarity betweeen users and based on raw ratings
user_similarity=cosine_similarity(user_item_matrix_filled)

#Convert the
user_similarity_df=pd.DataFrame(user_similarity,index=user_item_matrix.index, columns=user_item_matrix.index)

#step 4: Function to get recoomendations for specific user based on 
def get_collabarative_recommendations_for_user(user_id, num_recommendations=5):
    #
    similar_users=user_similarity_df[user_id].sort_values(ascending=False)
    #Get the most similar users(excluding the users themselves ) 
    similar_users=similar_users.drop(user_id)
    
    #Select the 
    top_similar_users=similar_users.head(50)
    
    #
    
    weighted_ratings=np.dot(top_similar_users.values,user_item_matrix_filled.loc[top_similar_users.index])
    sum_of_similarities=top_similar_users.sum()
    #np.dot: This computes the dot product between the 
    #similarity scores of the top similar users and
    #their corresponding ratings in the user-item matrix.
    #The result is an array of weighted ratings for each game.
    #Normalize by the sum of similarities
    if sum_of_similarities>0:
        weighted_ratings /= sum_of_similarities
        #the weighted ratings are normalizes by dividing by the 
        #sum of similarities too avoid biasing towards users with higher ratings 
        
    #
    user_ratings=user_item_matrix_filled.loc[user_id]
    unrated_games=user_ratings[user_ratings==0]


    #
    game_recommendations=pd.Series(weighted_ratings, index=user_item_matrix_filled.columns).loc[unrated_games.index]
    #
    return game_recommendations.sort_values(ascending =False).head(num_recommendations)

recommended_games=get_collabarative_recommendations_for_user(user_id=3)

#print() the recommnded games
print('Recommended games for users 3 : ')
print(recommended_games)














