from flask import Flask,jsonify,request
from demographic_filtering import output
from storage import all_movies,liked_movies,non_liked_movies,non_match_movies
from content_filtering import get_recommendations
import csv

with open('Movies - Movies.csv') as f:
    reader = csv.reader(f)
    data=list(reader)
    allMovies=data[1:]
# print(allMovies[0])

liked_movies=[]
non_liked_movies=[]
did_not_match=[]


app=Flask(__name__)

@app.route('/get-movie')

def get_movie():
    movie_data={"title":all_movies[0][19],
                "poster_link": all_movies[0][27],
                "release_date":all_movies[0][13],
                "duration":all_movies[0][15], 
                "rating":all_movies[0][20], 
                "overview":all_movies[0][9]}
    return jsonify({'data':movie_data,'status':movie_data,'Sucsess':movie_data}),201

@app.route('/liked-movie',methods=["POST"])

def liked_movie():
    allMovies=allMovies[1:]
    movies=allMovies[0]
    liked_movies.append(movies)
    allMovies.pop()
    return jsonify({'status':'Sucsess'}),201

@app.route('/non-liked-movie',methods=["POST"])

def dis_liked_movie():
    allMovies=allMovies[1:]
    movies=allMovies[0]
    non_movies.append(movies)
    allMovies.pop()
    return jsonify({'status':'Sucsess'}),201

@app.route('/did-not-match',methods=["POST"])

def non_match():
    allMovies=allMovies[1:]
    movies=allMovies[0]
    did_not_match.append(movies)
    allMovies.pop()
    return jsonify({'status':'Sucsess'}),201

@app.route('/popular-movies',methods=['POST'])

def popular_movies():
    movie_data=[]
    for movie in output:
        z={"title":movie[0],
            "poster_link": movie[1],
            "release_date":movie[2],
            "duration":movie[3] or 'N/A', 
            "rating":movie[4], 
            "overview":movie[5]}
        movie_data.append(z)
    return jsonify({
        'data':movie_data,
        'status':"Sucsess"
    }),200

@app.route('/get-movie-recomendations',methods=['POST'])

def get_recomendations():
    all_recomended=[]
    for liked_movie in liked_movies:
        output=get_recomendations(liked_movie[0])
        for data in output:
            all_recomended.append(data)
        import itertools
        all_recomended.sort()
        all_recomended=list(all_recomended for all_recomended,_ in itertools.groupby(all_recommended))
        movie_data=[]
        for recomendation in all_recomended:
             d={"title":movie[0],
               "poster_link": movie[1],
               "release_date":movie[2],
               "duration":movie[3] or 'N/A', 
               "rating":movie[4], 
               "overview":movie[5]}
        movie_data.append(d)
    return jsonify({
        'data':movie_data,
        'status':'Sucsess'
    }),200

if __name__ == '__main__':
    app.run(host="localhost", port= 5000,debug=True)
    

