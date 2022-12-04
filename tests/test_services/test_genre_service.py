import pytest
from unittest.mock import MagicMock
from service.genre import GenreService


class TestGenreService():
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_all(self):
        genres = self.genre_service.get_all(filters={})
        assert genres is not None
        assert len(genres) > 0

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id == 1
        assert genre.name == "genre1"

    def test_create(self):
        data = {"id": 4, "name": "genre4"}
        genre = self.genre_service.create(data)
        assert genre is not None
        assert genre.id == 4
        assert genre.name == "genre4"

    def test_update(self):
        data = {"id": 4, "name": "genre4"}
        assert self.genre_service.update(data)

    def test_delete(self):
        assert self.genre_service.delete(1) is None
