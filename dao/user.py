from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def update(self, user_data):
        user = self.get_one(user_data.get("id"))
        if user_data.get("name") is not None:
            user.name = user_data.get("name")
        if user_data.get("surname") is not None:
            user.surname = user_data.get("surname")
        if user_data.get("favorite_genre") is not None:
            user.favorite_genre = user_data.get("favorite_genre")

        self.session.add(user)
        self.session.commit()

    def update_password(self, data):
        user = self.get_by_email(data.get("email"))
        if data.get("password_2") is not None:
            user.password = data.get("password_2")

        self.session.add(user)
        self.session.commit()

    def create(self, user_data):
        user = User(**user_data)

        self.session.add(user)
        self.session.commit()
        return user
