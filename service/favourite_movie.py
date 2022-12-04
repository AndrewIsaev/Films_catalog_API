class FavouriteMovieService:
    def __init__(self, dao):
        self.dao = dao

    def create(self, data):
        return self.dao.create(data)

    def delete(self, mid):
        return self.dao.delete(mid)