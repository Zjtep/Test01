from flask import Blueprint, jsonify, request
import sqlite3

# from . import db
# from .models import Movie

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

main = Flask(__name__)

# main.config['SQLALCHEMY_TRRACK_MODIFICATIONS'] =False
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(main)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    rating = db.Column(db.Integer)


@main.route('/add_movies', methods=['POST'])
def add_movie():
    movie_data = request.get_json()

    new_movie = Movie(title=movie_data['title'], rating=movie_data['rating'])

    db.session.add(new_movie)
    db.session.commit()

    return jsonify({'movies': "asdgh"})


@main.route('/movies', methods=['GET', 'POST'])
def movies():
    if (request.method == 'GET'):
        movie_list = Movie.query.all()
        movies = []

        for movie in movie_list:
            movies.append({'title': movie.title, 'rating': movie.rating})

        return jsonify({'movies': movies})
    else:
        movie_data = request.get_json()

        new_movie = Movie(title=movie_data['title'], rating=movie_data['rating'])

        db.session.add(new_movie)
        db.session.commit()

        return jsonify({'movies': "asdgh"})


if __name__ == '__main__':
    main.run(debug=True)
