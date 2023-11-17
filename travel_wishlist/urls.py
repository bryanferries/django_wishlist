from django.urls import path
from . import views
                # These are the "urls" but they are actually just on the computer as a server
urlpatterns = [
    path('', views.place_list, name='place_list'),
    path('visited', views.places_visited, name='places_visited'),
    path('place_in_bob/<int:place_pk>/was_visited', views.place_was_visited, name='place_was_visited'),
    path('about', views.about, name='about')
]