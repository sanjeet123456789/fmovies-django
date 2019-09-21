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
from .views_delete import *
from django.views.generic import RedirectView
urlpatterns = [
    path("",Index,name="movies-index"),
    path("movies/<int:movies_id>/",Movies_detail,name="movies-detail"),
    path("genre/<str:genre_name>",Genre_detail,name="genre-detail"),
    path("cast/<str:cast_name>",Cast_detail,name="cast-detail"),
    path("director/<str:director_name>",Director_detail,name="director-detail"),
    path("writer/<str:writer_name>",Writer_detail,name="writer-detail"),
    path("award/<str:award_name>",Award_detail,name="award-detail"),
    path("country/<str:country_name>",Country_detail,name="country-detail"),
    path("language/<str:language_name>",Language_detail,name="language-detail"),
    path("movies-type/<str:movies_type_name>",Movies_type_detail,name="movies_type-detail"),
    path("quality/<str:quality_name>",Quality_detail,name="quality-detail"),
    path("contact/",Contact_list,name="fmovies-contact"),


  

    path('ajax/load-cast/', load_cast, name='ajax_load_cast'),
    path('ajax/load-genre/', load_genre, name='ajax_load_genre'),
    path('ajax/load-director/', load_director, name='ajax_load_director'),
    path('ajax/load-writer/', load_writer, name='ajax_load_writer'),
    path('ajax/load-award/', load_award, name='ajax_load_award'),
    path('ajax/load-language/', load_language, name='ajax_load_language'),
    path('', RedirectView.as_view(pattern_name='movies-index'),name='home'),

    path('award/<int:award_id>/delete/',Award_list_delete,name="award-list-delete"),
    path('cast/<int:cast_id>/delete/',Cast_list_delete,name="cast-list-delete"),
    path('director/<int:director_id>/delete',Director_list_delete,name="director-list-delete"),
    path('writer/<int:writer_id>/delete',Writer_list_delete,name="writer-list-delete"),
    path('country/<int:country_id>/delete',Country_list_delete,name="country-list-delete"),
    path('genre/<int:genre_id>/delete',Genre_list_delete,name="genre-list-delete"),
    path('language/<int:language_id>/delete',Language_list_delete,name="language-list-delete"),
    path('quality/<int:quality_id>/delete',Quality_list_delete,name="quality-list-delete"),
    path('server/<int:server_id>/delete',Server_list_delete,name="server-list-delete"),
    path('content-type/<int:server_type_id>/delete',Content_type_list_delete,name="content-type-list-delete"),
    path('subtitle/<int:subtitle_id>/delete',Subtitle_list_delete,name="subtitle-list-delete"),
    path('movies-type/<int:movies_type_id>/delete',Movies_type_list_delete,name="movies-type-list-delete"),
    path('movies/<int:movies_id>/delete',Movies_delete,name='movies-delete'),
    path('season/<int:season_id>/delete',Season_delete,name='season-delete'),
    path('episode/<int:episode_id>/delete',Episode_delete,name='episode-delete'),
    path('link/<int:link_id>/delete',Link_delete,name='link-delete'),

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