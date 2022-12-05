from sqlalchemy import desc

from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all_paginate(self, page, per_page):
        return self.session.query(Movie).paginate(page=page, per_page=per_page).items

    def get_all(self):
        return self.session.query(Movie).all()

    def filter_by_year(self):
        return self.session.query(Movie).order_by(desc(Movie.year)).all()

    def filter_by_year_paginate(self, page, per_page):
        return self.session.query(Movie).order_by(desc(Movie.year)).paginate(page=page, per_page=per_page).items

