from sqlalchemy.orm import relationship

from setup_db import db
from marshmallow import Schema, fields


class FavouriteMovie(db.Model):
    __tablename__ = "favourite_movies"

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = relationship("User")
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), primary_key=True)
    movie = relationship("Movie")


class FavouriteMovieShema(Schema):
    user_id = fields.Int()
    movie_id = fields.Int()

