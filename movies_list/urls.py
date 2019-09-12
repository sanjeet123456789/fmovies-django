from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    # PostListView,
    # PostDetailView,
    Award_list_create,
    Cast_list_create,
    # AwardCreateView,
    # PostUpdateView,
    # PostDeleteView,
    # UserPostListView
)
from .views import *
urlpatterns = [
    path('award/new/',Award_list_create,name="award-list-create"),
    path('cast/new/',Cast_list_create,name="cast-list-create"),
    path('director/new/',Director_list_create,name="director-list-create"),
    path('writer/new/',Writer_list_create,name="writer-list-create"),
    path('country/new/',Country_list_create,name="country-list-create"),
    path('genre/new/',Genre_list_create,name="genre-list-create"),
    path('language/new/',Language_list_create,name="language-list-create"),
    path('quality/new/',Quality_list_create,name="quality-list-create"),
    path('server/new/',Server_list_create,name="server-list-create"),
    path('content-type/new/',Content_type_list_create,name="content-type-list-create"),
    path('subtitle/new/',Subtitle_list_create,name="subtitle-list-create"),
    path('movies-type/new/',Movies_type_list_create,name="movies-type-list-create"),
    path('movies/new/',Movies_create,name='movies-create'),
    path('season/new/',Season_create,name='season-create'),
    path('episode/new/',Episode_create,name='episode-create'),
    path('link/new/',Link_create,name='link-create')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)