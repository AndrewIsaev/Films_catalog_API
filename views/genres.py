from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):

    def get(self):
        filters = {"page": request.args.get("page")}
        return GenreSchema(many=True).dump(genre_service.get_all(filters)), 200



@genre_ns.route('/<int:gid>')
class GenreView(Resource):

    def get(self, gid):
        r = genre_service.get_one(gid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200


