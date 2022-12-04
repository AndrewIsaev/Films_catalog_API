import pytest
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name="director1")
    director_2 = Director(id=2, name="director2")
    director_3 = Director(id=3, name="director3")

    directors = {1: director_1, 2: director_2, 3: director_3}

    director_dao.get_all = MagicMock(return_value=directors.values())
    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.create = MagicMock(return_value=Director(id=4, name="director4"))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name="genre1")
    genre_2 = Genre(id=2, name="genre2")
    genre_3 = Genre(id=3, name="genre3")

    genres = {1: genre_1, 2: genre_2, 3: genre_3}

    genre_dao.get_all = MagicMock(return_value=genres.values())
    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.create = MagicMock(return_value=Genre(id=4, name="genre4"))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie1 = Movie(
        id=1,
        title="title1",
        description="description1",
        trailer="trailer1",
        year=2001,
        rating=1.0,
        genre_id=1,
        director_id=1)

    movie2 = Movie(
        id=2,
        title="title2",
        description="description2",
        trailer="trailer2",
        year=2002,
        rating=2.0,
        genre_id=2,
        director_id=2)

    movie3 = Movie(
        id=3,
        title="title3",
        description="description3",
        trailer="trailer3",
        year=2003,
        rating=3.0,
        genre_id=3,
        director_id=3)

    movies = {1: movie1, 2: movie2, 3: movie3}

    movie_dao.get_all = MagicMock(return_value=movies.values())
    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.create = MagicMock(return_value=Movie(
        id=4,
        title="title4",
        description="description4",
        trailer="trailer4",
        year=2004,
        rating=4.0,
        genre_id=4,
        director_id=4))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao
