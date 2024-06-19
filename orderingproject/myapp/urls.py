from django.urls import path
from .views import movies_by_year_and_actor

urlpatterns = [
    path('movies/', movies_by_year_and_actor, name='movies_by_year_and_actor'),
]
