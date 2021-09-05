# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:28:41 2020

@author: DELL
"""

import os
from flask import Flask, jsonify, Response

app = Flask(__name__, instance_relative_config=True)

movie_list = {"Citation": {"views": 200, "movie_id": 0, "genre": "Action", "rate": 4, "likes": 300}, "Blacklist":
    {"views": 150, "movie_id": 1, "genre": "horror", "rate": 6, "likes": 500}}


@app.route("/api/")
def index():
    return "Welcome to my first API project"


@app.route("/api/video/", methods=["GET"])
def get():
    return jsonify(movie_list)


@app.route("/api/video/<int:movie_id>/", methods=["GET"])
def get_movie_id(movie_id):
    return jsonify({list(movie_list.keys())[movie_id]: movie_list[list(movie_list.keys())[movie_id]]})


def if_movie_doesnt_exist(movie_name):
    if movie_name not in movie_list.keys():
        return {movie_name: "Movie name does not exit"}


@app.route("/api/video/<string:movie_name>/", methods=["GET"])
def get_movie_name(movie_name):
    if movie_name not in movie_list.keys():
        return {movie_name: "Movie name does not exit"}
    return jsonify({movie_name: movie_list[movie_name]})


@app.route("/api/video/<string:movie_name>/", methods=["POST"])
def post(movie_name):
    newMovie = {"Black Panther": {"view": 500, "movie_id": 2, "genre": "Action", "likes": 700}}
    movie_list.append(newMovie)
    return jsonify({"List": movie_list})


@app.route("/api/video/<string:movie_name>/", methods=["PUT"])
def put(movie_name):
    if_movie_doesnt_exist(movie_name)
    movie_list[movie_name]["views"] = 50000
    return jsonify({"List": movie_list})


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
