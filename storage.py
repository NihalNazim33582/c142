import csv

liked_movies=[]
non_liked_movies=[]
non_match_movies=[]

all_movies=[]
with open('final.csv',encoding='utf8') as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]

