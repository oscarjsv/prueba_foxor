import requests
from collections import defaultdict
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv
import os


load_dotenv()

# Obtener API_KEY desde las variables de entorno
API_KEY = os.getenv('API_KEY')
BASE_URL = 'http://www.omdbapi.com/'


def get_movies(query):
    movies = []
    page = 1
    while True:
        response = requests.get(
            BASE_URL, params={'apikey': API_KEY, 's': query, 'type': 'movie', 'page': page})
        if response.status_code != 200:
            break
        data = response.json()
        if 'Search' in data:
            movies.extend(data['Search'])
        else:
            break
        if page >= (int(data.get('totalResults', 0)) // 10 + 1):
            break
        page += 1
    return movies


def get_movie_details(imdb_id):
    response = requests.get(BASE_URL, params={'apikey': API_KEY, 'i': imdb_id})
    if response.status_code == 200:
        return response.json()
    return {}


def group_movies_by_year_and_actor(movies):
    grouped_data = defaultdict(lambda: defaultdict(int))

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(
            get_movie_details, movie['imdbID']): movie['imdbID'] for movie in movies}

        for future in as_completed(futures):
            imdb_id = futures[future]
            try:
                details = future.result()
                year = details.get('Year')
                if year is None:
                    continue
                actors = details.get('Actors', '').split(', ')
                for actor in actors:
                    grouped_data[year][actor] += 1
            except Exception as e:
                logger.error(f"Error processing movie {imdb_id}: {e}")

    return grouped_data


@require_GET
def movies_by_year_and_actor(request):
    query = request.GET.get('query', 'Batman')
    movies = get_movies(query)
    grouped_data = group_movies_by_year_and_actor(movies)
    return JsonResponse(grouped_data, safe=False)
