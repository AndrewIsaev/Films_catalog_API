from dao.model.favourite_movie import FavouriteMovie

class FavouriteMovieDAO:
    def __init__(self, session):
        self.session = session

    def create(self, data):
        f_movie = FavouriteMovie(**data)
        self.session.add(f_movie)
        self.session.commit()
        return f_movie

    def delete(self, mid):
        f_movie = self.session.query(FavouriteMovie).get(mid)
        self.session.delete(f_movie)
        self.session.commit()
