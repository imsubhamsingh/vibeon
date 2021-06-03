"""vibeon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from playlists.views import (
    MovieListView,
    FeaturedPlaylistListView,
    PlaylistDetailView,
    MovieDetailView,
    TVShowListView,
    TVShowDetailView,
    TVShowSeasonDetailView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("category/", include("categories.urls")),
    path("categories/", include("categories.urls")),
    path("", FeaturedPlaylistListView.as_view()),
    path("movies/", MovieListView.as_view()),
    path("movies/<slug:slug>/", MovieDetailView.as_view()),
    path("media/<int:pk>/", PlaylistDetailView.as_view()),
    path("shows/", TVShowListView.as_view()),
    path("shows/<slug:slug>/", TVShowDetailView.as_view()),
    path("shows/<slug:slug>/seasons/", TVShowDetailView.as_view()),
    path(
        "shows/<slug:showSlug>/seasons/<slug:seasonSlug>/",
        TVShowSeasonDetailView.as_view(),
    ),
]
