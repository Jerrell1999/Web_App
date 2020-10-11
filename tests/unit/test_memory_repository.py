from datetime import date, datetime
from typing import List

import pytest

from movie.domainmodel.movie import Movie
from movie.adapters.repository import RepositoryException


def test_repository_can_retrieve_movie_count(in_memory_repo):
    number_of_movies = in_memory_repo.get_number_of_movies()

    # Check that the query returned 5 Movie.
    assert number_of_movies == 5


def test_repository_can_add_movie(in_memory_repo):
    movie = Movie(
        'Finding Potato',
        2020
    )
    movie.rank = 6
    in_memory_repo.add_movie(movie)

    assert in_memory_repo.get_movie(6) is movie
    assert in_memory_repo.get_movie(6).rank == 6


def test_repository_does_not_retrieve_a_non_existent_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(101)
    assert movie is None


def test_repository_can_retrieve_articles_by_rank(in_memory_repo):
    movie = in_memory_repo.get_movie_by_rank(5)

    # Check that the query returned Movie that is ranked 5.
    assert movie.rank == 5


def test_repository_does_not_retrieve_a_movie_when_there_are_no_movie_of_that_given_rank(in_memory_repo):
    movie = in_memory_repo.get_movie_by_rank(69)
    assert movie == None


def test_repository_can_get_first_movie(in_memory_repo):
    movie = in_memory_repo.get_first_movie()
    assert movie.title == 'Guardians of the Galaxy'


def test_repository_can_get_last_movie(in_memory_repo):
    movie = in_memory_repo.get_last_movie()
    assert movie.title == 'Suicide Squad'


def test_repository_returns_rank_of_previous_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(2)
    previous_rank = in_memory_repo.get_previous_movie_by_rank(movie)

    assert previous_rank == 1


def test_repository_returns_none_when_there_are_no_previous_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(1)
    previous_rank = in_memory_repo.get_previous_movie_by_rank(movie)

    assert previous_rank is None


def test_repository_returns_rank_of_next_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(2)
    next_rank = in_memory_repo.get_next_movie_by_rank(movie)

    assert next_rank == 3


def test_repository_returns_none_when_there_are_no_subsequent_articles(in_memory_repo):
    movie = in_memory_repo.get_movie(5)
    next_rank = in_memory_repo.get_next_movie_by_rank(movie)

    assert next_rank is None
