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
from .views_update import *
urlpatterns = [
    path("",Index,name="movies-index"),
    path("movies/<int:movies_id>/",Movies_detail,name="movies-detail"),

    path('award/<int:award_id>/update',Award_list_update,name="award-list-update"),
    path('cast/<int:cast_id>/update',Cast_list_update,name="cast-list-update"),
    path('director/<int:director_id>/update',Director_list_update,name="director-list-update"),
    path('writer/<int:writer_id>/update',Writer_list_update,name="writer-list-update"),
    path('country/<int:country_id>/update',Country_list_update,name="country-list-update"),
    path('genre/<int:genre_id>/update',Genre_list_update,name="genre-list-update"),
    path('language/<int:language_id>/update',Language_list_update,name="language-list-update"),
    path('quality/<int:quality_id>/update',Quality_list_update,name="quality-list-update"),
    path('server/<int:server_id>/update',Server_list_update,name="server-list-update"),
    path('content-type/<int:server_type_id>/update',Content_type_list_update,name="content-type-list-update"),
    path('subtitle/<int:subtitle_id>/update',Subtitle_list_update,name="subtitle-list-update"),
    path('movies-type/<int:movies_type_id>/update',Movies_type_list_update,name="movies-type-list-update"),
    path('movies/<int:movies_id>/update',Movies_update,name='movies-update'),
    path('season/<int:season_id>/update',Season_update,name='season-update'),
    path('episode/<int:episode_id>/update',Episode_update,name='episode-update'),
    path('link/<int:link_id>/update',Link_update,name='link-update'),

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