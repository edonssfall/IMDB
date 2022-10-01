import json
import os.path
import time
from django.core.management.base import BaseCommand
from apps.imdb.models import Movie, Person, PersonMovie


class Command(BaseCommand):
    help = 'Import Person Movies from IMDB tsv'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', type=str)

    def handle(self, *args, **options):
        print("(+)Processing...")
        start_time = time.time()
        attempts = 0
        file_tsv = options.get('file')
        if os.path.exists('file'):
            print('File not exist')
        with open(file_tsv, 'r') as tsv:
            for line in tsv.readlines():
                if not line:
                    continue
                if not line.startswith('tt'):
                    continue
                data = line.split('\t')
                movie_id = Movie.objects.filter(imdb_id=data[0]).first()
                if not movie_id:
                    continue
                person_id = Person.objects.filter(imdb_id=data[2]).first()
                if not person_id:
                    continue
                characters = data[5]
                if characters.startswith('\\N'):
                    characters = None
                else:
                    characters = json.loads(characters)
                person_movie_data = {
                    'order': int(data[1]),
                    'job': data[3],
                    'characters': characters
                }
                person_movie, created = PersonMovie.objects.get_or_create(
                    movie_id=movie_id,
                    person_id=person_id,
                    defaults=person_movie_data
                )
                if created:
                    PersonMovie.objects.filter(id=person_movie.id).update(**person_movie_data)
                if attempts % (1 << 20) == 0:
                    print(
                        f"Debug control: Attempts = {attempts} | PersonMovies = {person_movie} | {time.time() - start_time}")
                attempts += 1
        print("Person Movies Import", "FINISH!!!", time.time() - start_time, sep='\n')
