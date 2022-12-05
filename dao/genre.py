from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Genre).get(bid)

    def get_all(self):
        return self.session.query(Genre).all()

    def get_all_paginate(self, page, per_page):
        return self.session.query(Genre).paginate(page=page, per_page=per_page).item

