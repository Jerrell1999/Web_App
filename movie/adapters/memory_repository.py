from typing import List

from movie.adapters.repository import AbstractRepository, RepositoryException

from bisect import bisect, bisect_left, insort_left

from movie.datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from movie.domainmodel.user import User
from movie.domainmodel.movie import Movie


class MemoryRepository(AbstractRepository):
    def __init__(self):
        self._movies_list = []
        self._actors_list = []
        self._directors_list = []
        self._genre_list = []

    def add_movie(self, movie: Movie):
        self._movies_list.append(movie)

    def get_movie(self, rank: int) -> Movie:
        movie = None

        try:
            for stored_movie in self._movies_list:
                if stored_movie.rank == rank:
                    movie = stored_movie
        except KeyError:
            pass  # Ignore exception and return None.

        return movie

    def get_movie_by_rank(self, target_rank: int) -> Movie:
        matching_movie_by_rank = None

        for movie in self._movies_list[0:target_rank]:
            if movie.rank == target_rank:
                matching_movie_by_rank = movie

        return matching_movie_by_rank

    def get_number_of_movies(self):
        return len(self._movies_list)

    def get_first_movie(self):
        return self._movies_list[0]

    def get_last_movie(self):
        return self._movies_list[-1]

    def get_previous_movie_by_rank(self, movie: Movie):
        previous_rank = None

        try:
            rank = movie.rank
            for stored_movie in reversed(self._movies_list[0:rank]):
                if stored_movie.rank < movie.rank:
                    previous_rank = stored_movie.rank
                    break
        except ValueError:
            # No earlier articles, so return None.
            pass

        return previous_rank

    def get_next_movie_by_rank(self, movie: Movie):
        next_rank = None

        try:
            rank = movie.rank
            for stored_movie in self._movies_list[rank:len(self._movies_list)]:
                if stored_movie.rank > movie.rank:
                    next_rank = stored_movie.rank
                    break
        except ValueError:
            # No subsequent articles, so return None.
            pass

        return next_rank


def load_movies(data_path: str, repo: MemoryRepository):
    movie_file_reader = MovieFileCSVReader(data_path)
    movie_file_reader.read_csv_file()

    for movie in movie_file_reader.dataset_of_movies:
        repo.add_movie(movie)


def populate(data_path: str, repo: MemoryRepository):
    load_movies(data_path, repo)
