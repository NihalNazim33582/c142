import pandas as pd
import numpy as np

df=pd.read_csv('final.csv')

c=df['vote_average'].mean()
print(c)

m=df['vote_count'].quantile(0.9)
print(m)

qmovie=df.copy().loc[df['vote_count']>=m]
print(qmovie.shape)

def weight_rating(x,m=m,c=c):
    v=x['vote_count']
    r=x['vote_average']
    return (v/(v+m)*r)+(m/(m+v)*c)

qmovie['Score']=qmovie.apply(weight_rating,axis=1)

qmovieSorted=qmovie.sort_values('Score',ascending=False)

output=qmovieSorted[['title_x','picture_links','release_date','runtime','vote_average','overview']].head(20).values.tolist()