from datetime import date

from flask import Blueprint, render_template
from flask import request, redirect, url_for, session

from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

import movie.adapters.repository as repo
import movie.news.services as services

# Configure Blueprint.
news_blueprint = Blueprint(
    'news_bp', __name__)


@news_blueprint.route('/movies_by_date', methods=['GET'])
def movies_by_date():

    target_rank = request.args.get('rank')

    first_movie = services.get_first_movie(repo.repo_instance)
    last_movie = services.get_last_movie(repo.repo_instance)

    if target_rank is None:
        target_rank = first_movie['rank']
    else:
        target_rank = int(target_rank)

    movie, previous_rank, next_rank = services.get_movie_by_rank(target_rank, repo.repo_instance)

    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if len(movie) > 0:
        if previous_rank is not None:
            prev_movie_url = url_for('news_bp.movies_by_date', rank=previous_rank)
            first_movie_url = url_for('news_bp.movies_by_date', rank=first_movie['rank'])

        if next_rank is not None:
            next_movie_url = url_for('news_bp.movies_by_date', rank=next_rank)
            last_movie_url = url_for('news_bp.movies_by_date', rank=last_movie['rank'])

        return render_template(
            'news/movies.html',
            movie_title=movie['title'],
            release_year=str(movie['release_year']),
            rank=str(movie['rank']),
            description=str(movie['description']),
            first_movie_url=first_movie_url,
            last_movie_url=last_movie_url,
            prev_movie_url=prev_movie_url,
            next_movie_url=next_movie_url,
        )

    return redirect(url_for('home_bp.home'))
