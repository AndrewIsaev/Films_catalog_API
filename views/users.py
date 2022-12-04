from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service
from decorators import auth_required
user_ns = Namespace("users")


@user_ns.route("/")
class UsersViews(Resource):
    @auth_required
    def get(self):
        users = user_service.get_all()
        return UserSchema(many=True).dump(users), 200

    @auth_required
    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route("/password")
class ChangeUserPassword(Resource):
    @auth_required
    def put(self):
        req_json = request.json
        user_service.update_password(req_json)
        return "", 201


@user_ns.route("/<int:uid>")
class UserViews(Resource):
    @auth_required
    def get(self, uid):
        user = user_service.get_one(uid)
        return UserSchema().dump(user), 200

    @auth_required
    def patch(self, uid):
        req_json = request.json
        req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    @auth_required
    def put(self):
        req_json = request.json
        user_service.update_password(req_json)
        return "", 204
