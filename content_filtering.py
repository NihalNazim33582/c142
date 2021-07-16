import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df=pd.read_csv('final.csv')
df=df[df['Soup'].notna()]
count=CountVectorizer(stop_words='english')
countMatrix=count.fit_transform(df['Soup'])
print(countMatrix.toarray())

cosine=cosine_similarity(countMatrix)
df = df.reset_index() 
indices = pd.Series(df.index, index=df['title_x'])



def get_recommendations(title):
    idex=indices[title]
    sim_scores=list(enumerate(cosine_sim[idex]))
    sim_scores=sorted(sim_scores,key=lambda x:x[1], reverse=True)
    sim_scores=sim_scores[1:11]
    movie_indices=[i[0] for i in sim_scores]
    return df[['title_x','picture_links','release_date','runtime','vote_average','overview']].iloc[movie_indices].values.tolist()