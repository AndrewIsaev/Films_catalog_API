import pytest
from unittest.mock import MagicMock

from service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_all(self):
        directors = self.director_service.get_all(filters={})
        assert directors is not None
        assert len(directors) > 0

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id == 1
        assert director.name == "director1"

    def test_create(self):
        data = {"id": 4, "name": "director4"}
        director = self.director_service.create(data)
        assert director is not None
        assert director.id == 4
        assert director.name == "director4"

    def test_update(self):
        data = {"id": 4, "name": "director4"}
        assert self.director_service.update(data)

    def test_delete(self):
        assert self.director_service.delete(1) is None
