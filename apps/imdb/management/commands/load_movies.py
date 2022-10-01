import os.path
import time
from django.core.management.base import BaseCommand
from apps.imdb.models import Movie


class Command(BaseCommand):
    help = "Import Movies from IMDB tsv"

    def add_arguments(self, parser):
        parser.add_argument("-f", "--file", type=str)

    def handle(self, *args, **options):
        print("(+)Processing...")
        start_time = time.time()
        attempts = 0
        file_tsv = options.get('file')
        if os.path.exists('file'):
            print("File not exist")
        with open(file_tsv, 'r') as tsv:
            for line in tsv.readlines():
                if not line:
                    continue
                if not line.startswith("tt"):
                    continue
                data = line.split('\t')
                if data[1] not in ['short', 'movie']:
                    continue
                data[8] = data[8][:-1]
                if data[8] == '\\N':
                    data[8] = None
                else:
                    genres = data[8].split(',')
                date = data[5]
                is_adult = data[4]
                if is_adult == '0':
                    is_adult = False
                else:
                    is_adult = True
                if date == '\\N':
                    date = None
                else:
                    date = f'{date}-01-01'
                data_movie = {
                    'title_type': data[1],
                    'name': data[2],
                    'is_adult': is_adult,
                    'year': date,
                    'genres': genres
                }
                _db_creat(Movie, data, data_movie)
                if attempts % (1 << 20) == 0:
                    print(f"Debug control: Attempts = {attempts} | Movie = {data[2]} | {time.time() - start_time}")
                attempts += 1
        print("Movies Import", "FINISH!!!", time.time() - start_time, sep='\n')


def _db_creat(model, data, data_model):
    db_data, created = model.objects.get_or_create(
        imdb_id=data[0],
        defaults=data_model
    )
    if created:
        model.objects.filter(id=db_data.id).update(**data_model)
