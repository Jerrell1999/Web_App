from typing import List, Iterable

from movie.adapters.repository import AbstractRepository
from movie.domainmodel.movie import Movie


class NonExistentArticleException(Exception):
    pass


class UnknownUserException(Exception):
    pass


def get_movie(movie_rank: int, repo: AbstractRepository):
    movie = repo.get_movie(movie_rank)

    if movie is None:
        raise NonExistentArticleException

    return movie_to_dict(movie)


def get_first_movie(repo: AbstractRepository):

    movie = repo.get_first_movie()

    return movie_to_dict(movie)


def get_last_movie(repo: AbstractRepository):

    movie = repo.get_last_movie()
    return movie_to_dict(movie)


def get_movie_by_rank(rank, repo: AbstractRepository):

    movie = repo.get_movie_by_rank(target_rank=rank)
    movies_dto = list()
    prev_rank = next_rank = None

    if movie.rank > 0:
        prev_rank = repo.get_previous_movie_by_rank(movie)
        next_rank = repo.get_next_movie_by_rank(movie)

        # Convert Movies to dictionary form.
        movies_dto = movie_to_dict(movie)

    return movies_dto, prev_rank, next_rank


# ============================================
# Functions to convert model entities to dicts
# ============================================

def movie_to_dict(movie: Movie):
    movie_dict = {
        'title': movie.title,
        'release_year': movie.release_year,
        'rank': movie.rank,
        'description': movie.description,
        'actors': movie.actors,
        'genres': movie.genres,
        'runtime_minutes': movie.runtime_minutes
    }
    return movie_dict

# ============================================
# Functions to convert dicts to model entities
# ============================================

def dict_to_article(dict):
    movie = Movie(dict.title, dict.release_year)
    # Note there's no comments or tags.
    return movie
