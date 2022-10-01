import time
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
            if movie.rank is not None:
                print(movie.imdb_id, movie.name, movie.rank, movie.poster_url)
                continue
            print(f'Processing {movie.imdb_id} {movie.name}')
            url = "https://imdb8.p.rapidapi.com/title/get-meta-data"

            querystring = {"ids": f"{movie.imdb_id}", "region": "US"}

            headers = {
                "X-RapidAPI-Key": RapidAPI,
                "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            json_file = response.json()
            if json_file[f'{movie.imdb_id}']['title'] is None:
                continue
            if 'image' not in json_file[f'{movie.imdb_id}']['title']:
                image_url = None
            else:
                image_url = json_file[f'{movie.imdb_id}']['title']['image']['url']
            if 'rating' not in json_file[f'{movie.imdb_id}']['ratings']:
                rating = None
            else:
                print(json_file[f'{movie.imdb_id}']['ratings']['rating'])
                rating = json_file[f'{movie.imdb_id}']['ratings']['rating']
            current_rank = json_file[f'{movie.imdb_id}']['popularity']['currentRank']
            data = {
                'poster_url': image_url,
                'rating_imdb': rating,
                'rank': current_rank
            }
            Movie.objects.filter(imdb_id=movie.imdb_id).update(**data)
            attempts += 1
            time.sleep(5)
            if attempts == 70:
                print(time.time() - start_time)
                break