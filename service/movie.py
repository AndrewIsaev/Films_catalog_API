from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self, filters):
        if filters.get("status") == "new" and filters.get("page") is not None:
            movies = self.dao.filter_by_year_paginate(page=filters.get("page"), per_page=12)
        elif filters.get("status") == "new":
            movies = self.dao.filter_by_year()
        elif filters.get("page") is not None:
            movies = self.dao.get_all_paginate(page=filters.get("page"), per_page=12)
        else:
            movies = self.dao.get_all()
        return movies

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, movie_d):
        self.dao.update(movie_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)
