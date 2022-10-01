import random
import time
from pathlib import Path
import bs4
import fake_useragent
import requests
from apps.imdb.models import Movie
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "To download write -a or --api then api key"

    def handle(self, *args, **options):
        print('(+)Processing')
        dir_path = Path.cwd()
        path = Path(dir_path)
        start_time = time.time()
        attempts = 0
        for movie in Movie.objects.all():
            time.sleep(5)
            session = requests.Session()
            user = fake_useragent.UserAgent().random
            headers = {
                'user-agent': user
            }
            default_link = 'https://www.imdb.com/'
            link = f'https://www.imdb.com/title/{movie}/'
            response = session.get(link, headers=headers)
            print(f'connected to {movie}')
            bs = bs4.BeautifulSoup(response.text, 'lxml')
            block_poster = bs.find('div',
                                   class_='ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width sc-d383958-0 '\
                                          'gvOdLN celwidget ipc-sub-grid-item ipc-sub-grid-item--span-2')
            if block_poster is None:
                continue
            link_storage = block_poster.find('a', class_='ipc-lockup-overlay ipc-focusable')
            if link_storage is None:
                continue
            time.sleep(random.randrange(5, 10))
            image_imdb_link = link_storage.get('href')
            image_imdb_response = session.get(f'{default_link}{image_imdb_link}', headers=headers)
            bs_imdb = bs4.BeautifulSoup(image_imdb_response.text, 'lxml')
            block_imb_poster = bs_imdb.find('div', class_='sc-7c0a9e7c-2 bkptFa')
            if block_imb_poster is None:
                continue
            link_image_amazon = block_imb_poster.find('img').get('src')

            update_data = {
                'poster_url': link_image_amazon
            }
            Movie.objects.filter(imdb_id=movie).update(**update_data)
            print(f'downloaded {attempts} || time: {time.time()-start_time}')
            attempts += 1
            time.sleep(random.randrange(5, 10))
