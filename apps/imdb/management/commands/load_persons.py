import os.path
import time
from django.core.management.base import BaseCommand
from apps.imdb.models import Person
from .load_movies import _db_creat


class Command(BaseCommand):
    help = 'Import Persons from IMDB tsv'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', type=str)

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
                if not line.startswith('nm'):
                    continue
                data = line.split('\t')
                birth_day = data[2]
                death_day = data[3]
                if birth_day == '\\N':
                    birth_day = None
                else:
                    birth_day = f'{birth_day}-01-01'
                if death_day == '\\N':
                    death_day = None
                else:
                    death_day = f'{death_day}-01-01'
                data_person = {
                    'name': data[1],
                    'birth_year': birth_day,
                    'death_year': death_day
                }
                _db_creat(Person, data, data_person)
                if attempts % (1 << 20) == 0:
                    print(
                        f"Debug control: Attempts = {attempts} | Person = {data[1]} | {time.time() - start_time}"
                    )
                attempts += 1
        print("Persons Import", "FINISH!!!", time.time() - start_time, sep='\n')
