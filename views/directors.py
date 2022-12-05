from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):

    # @director_ns.doc(params={"123": 123})
    def get(self):
        page = request.args.get("page")
        filters = {"page": page}
        return DirectorSchema(many=True).dump(director_service.get_all(filters)), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):

    def get(self, did):
        r = director_service.get_one(did)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200
