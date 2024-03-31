from django.urls import path, re_path

import theatre.views as theatre

urlpatterns = [
    path('', theatre.page_cinema, name="main_url"),
    path('<slug:movie_slug>/', theatre.movie),
]