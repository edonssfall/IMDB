import time
import fake_useragent
from apps.imdb.models import Movie
from django.core.management import BaseCommand
from .API_keys import *
import requests


class Command(BaseCommand):
    help = "To download write API keys from rapid or imdb-api to file API_keys as RapidAPI and IMDB_API"

    def handle(self, *args, **options):
        print('(+)Processing')
        start_time = time.time()
        attempts = 0
        for movie in Movie.objects.all():
            # !!!To use API https:://imdb-api.com!!!
            if movie.poster_url is not None or movie.poster_url != '':
                session = requests.Session()
                user = fake_useragent.UserAgent().random
                headers = {
                    'user-agent': user
                }
                link = f'https://imdb-api.com/en/API/Title/{IMDB_API}/{movie.imdb_id}/Posters,Ratings'
                response = session.get(link, headers=headers)
                data = response.json()
                rating_imdb = data['imDbRating']
                posters_url = data['posters']['posters']
                poster_url = ''
                if len(posters_url) > 0:
                    poster_url = posters_url['0']['link']
                data_model = {
                    'poster_url': poster_url,
                    'rating_imdb': rating_imdb
                }
                Movie.objects.filter(imdb_id=movie.imdb_id).update(**data_model)
                if attempts % (1 << 20) == 0:
                    print(f"Debug control: Attempts = {attempts} | Movie = {movie.imdb_id} | {time.time() - start_time}")
                attempts += 1
                print(rating_imdb, poster_url)
                if attempts == 80:
                    print('80 Ready')
                    break
