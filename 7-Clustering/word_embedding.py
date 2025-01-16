# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 09:19:35 2024

@author: samir
"""

import gensim
print(gensim.__version__)
import pandas as pd 
df=pd.read_json("Cell_Phones_and_Accessories_5.json",lines=True)
df
df.shape
#
review_text=df.reviewText.apply(gensim.utils.simple_preprocess)
review_text
#
review_text.loc[4]
df.reviewText.loc[0]
#
model=gensim.models.Word2Vec(window=10,min_count=2,workers=4)
model
model.build_vocab(review_text,progress_per=1000)
#
#
#
#
model.train(review_text,total_examples=model.corpus_count,epochs=model.epochs)
model.save("D:/8-Text-Mining/text_mining/Word2vec-amazon-cell-accessories-reviews-short.model")
model.wv.most_similar('bud')
model.wv.similarity(w1='cheap',w2='inexpensive')
model.wv.similarity(w1='great',w2='good')

                    












