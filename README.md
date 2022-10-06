# IMDB

## Quick Start
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- docker-compose up
- docker exec -it docker_web_name bash
- python3 manage.py migrate
- ./manage.py loaddata db.json