# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 08:35:51 2024

@author: samir
"""

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
#sample dataset
transactions=[
['Milk','Bread','Butter'],
['Bread','Eggs'],
['Milk','Bread','Eggs','Butter'],
['Bread','Eggs','Butter'],
['Milk','Bread','Eggs']        
]


##step 1:Convert a dataset into suitable format for apriori
te=TransactionEncoder()
te_ary=te.fit(transactions).transform(transactions)
df=pd.DataFrame(te_ary,columns=te.columns_)
#step 2: Apply the apriopri alorithm to find frequent itemsets
frequent_itemsets=apriori(df,min_support=0.5,use_colnames=True)

#step 3: Generate the association rules from the frequent itemsets
rules=association_rules(frequent_itemsets,metric='lift',min_threshold=1)
#step4:output the results
print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules: ")
print(rules[['antecedents','consequents','support','confidence','lift']])

healthcare_data=[
    ['Fever','Cough','Covid-19'],
    ['Cough','Sore Throat','Flu'],
    ['Fever','Cough','Shortness of Breath','Covid-19'],
    ['Cough','Sore Throat','Flu','Headache'],
    ['Fever','Body Ache','Flu'],
    ['Fever','Cough','Covid-19','Shortness of Breath'],
    ['Sore Throat','Headache','Cough'],
    ['Body Ache','Fatigue','Flu']
]


te=TransactionEncoder()
te_ary=te.fit(healthcare_data).transform(healthcare_data)
d=pd.DataFrame(te_ary,columns=te.columns_)
#step 2: Apply the apriopri alorithm to find frequent itemsets
frequent_itemsets=apriori(d,min_support=0.3,use_colnames=True)

#step 3: Generate the association rules from the frequent itemsets
rules=association_rules(frequent_itemsets,metric='confidence',min_threshold=0.7)
#step4:output the results
print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules: ")
print(rules[['antecedents','consequents','support','confidence','lift']])





'''

'''





