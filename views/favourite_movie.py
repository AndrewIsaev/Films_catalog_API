from flask import request
from flask_restx import Namespace, Resource

from implemented import f_movie_service

f_movie_ns = Namespace("favorites")


@f_movie_ns.route("/movies/<int:mid>")
class FavouriteMovieView(Resource):
    def post(self, mid):
        req_json = request.json
        user_id = req_json.get("user_id")
        data = {
            "user_id": user_id,
            "movie_id": mid
        }
        f_movie_service.create(data)
        return "Add", 201

    def delete(self, mid):
        f_movie_service.delete(mid)
        return "", 204
