import abc
from movie.domainmodel.user import User
from movie.domainmodel.movie import Movie
from movie.domainmodel.genre import Genre
from movie.domainmodel.review import Review

repo_instance = None


class RepositoryException(Exception):
    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        """ Adds an Movie to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, title: str) -> Movie:
        """ Returns Movie with title from the repository.

        If there is no Movie with the given id, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_rank(self, target_rank: int) -> Movie:
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self):
        """ Returns the number of Movies in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_movie(self) -> Movie:
        """ Returns the first movie, ordered by rank, from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movie(self) -> Movie:
        """ Returns the last movie, ordered by rank, from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_previous_movie_by_rank(self, movie: Movie):
        """ Returns the title of an Movie that immediately precedes movie.

        If movie is the first Movie in the repository, this method returns None because there are no Movie
        on a previous title.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_next_movie_by_rank(self, movie: Movie):
        """ Returns the title of an Movie that immediately follows title.

        If movie is the last Movie in the repository, this method returns the first Movie.
        """
        raise NotImplementedError

