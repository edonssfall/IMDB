import time
from apps.imdb.models import Person
from django.core.management import BaseCommand
from .API_keys import *
import requests


class Command(BaseCommand):
    help = "To download write API keys from rapid or imdb-api to file API_keys as RapidAPI and IMDB_API"

    def handle(self, *args, **options):
        print('(+)Processing')
        start_time = time.time()
        attempts = 0
        for person in Person.objects.all():
            if person.image_url is not None or person.birth_place is not None:
                print('PASS', person.imdb_id, person.name)
                continue
            print(f'Processing {person.imdb_id} {person.name}')
            url = "https://imdb8.p.rapidapi.com/actors/get-bio"

            querystring = {"nconst": f"{person.imdb_id}"}

            headers = {
                "X-RapidAPI-Key": RapidAPI,
                "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            json_file = response.json()
            if json_file['name'] is None:
                continue
            if 'image' not in json_file:
                image_url = None
            else:
                image_url = json_file['image']['url']
            if 'birthPlace' not in json_file:
                birth_place = None
            else:
                birth_place = json_file['birthPlace']
            data = {
                'image_url': image_url,
                'birth_place': birth_place
            }
            Person.objects.filter(imdb_id=person.imdb_id).update(**data)
            attempts += 1
            time.sleep(5)
            if attempts == 499:
                print(time.time() - start_time)
                break