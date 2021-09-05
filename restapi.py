# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:12:21 2020

@author: Asimi
"""
#!pip install flask_restful
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

movieList = {"Citation": {"views":1000, "likes":200, "rate":12, "genre":"commedy"}, "Blaklist":{"views":500, "likes":240, "rate":4, "genre":"Action"}}

class video(Resource):
    
    def if_movie_doesnt_exist(movie_name):
        if movie_name not in movieList.keys():
            return {movie_name: "Movie name does not exit"}

    def if_movie_does_exist(movie_name):
        if movie_name in movieList.keys():
            return {movie_name: f"{movie_name} is already existing in the db"}
    
    def get(self, movie_name):
        if_movie_doesnt_exist(movie_name)
        return {movie_name: movieList[movie_name]}
    
    def post(self, movie_name):
        if_movie_doesnt_exist(movie_name)
        print(request.Form(movie_name))
        return {movie_id: movieList[movie_id]}
                
    def put(self, movie_id):
        if_movie_doesnt_exist(movie_name)
        movieList[movie_id] = 5
        return {movieList}

api.add_resource(video, "/video/<string:movie_name>/")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)