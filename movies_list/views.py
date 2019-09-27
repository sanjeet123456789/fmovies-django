from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Max
from math import ceil
from django.views.generic import(
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView


	)
from .models import Award_list
from .forms import *

def Index(request):
	movies_index=Movies_list.objects.all()
	all_Genre=[]
	catmovies=Movies_list.objects.values('genre','movies_id')
	cats={item['genre'] for item in catmovies}
	for cat in cats:
		movie=Movies_list.objects.filter(genre=cat)
		n=len(movie)
		nSlides=n//4 + ceil((n/4)-(n//4))
		all_Genre.append([movie,range(1,nSlides),nSlides])

	context={
		'all_Genre':all_Genre
		# "categories":movies_categories
	}
	return render(request,"movies_list/index.html",context)

def Search_list(request):
    movies_list = Movies_list.objects.all()
    movies_filter = SearchFilter(request.GET, queryset=movies_list)
    return render(request, 'movies_list/search_details.html', {'filter': movies_filter})




# def Search_list(request):
# 	query = request.GET.get('search')
# 	# if request.method=="GET":
# 	# 	print("this is get method")

# 	movies_details=Movies_list.objects.filter(name__contains=query)|Movies_list.objects.filter(story_line__contains=query)

# 	language_fill=Language_list.objects.all()
# 	languagex = request.GET.getlist('language')
# 	print(languagex)
# 	for el in languagex:
# 		print(el)
# 	# movies_details=movies_details.filter(story_line__contains="mercy")
# 	paginator=Paginator(movies_details,5)
# 	page=request.GET.get('page')
# 	movies_detail=paginator.get_page(page)


# 	context={
# 		"query":query,
# 		"movies_detail":movies_detail,
# 		"movies_details":movies_details,
# 		"language_fill":language_fill

# 	}
# 	return render(request,"movies_list/search_details.html",context)


def Movies_detail(request,movies_id):
	movies_details=Movies_list.objects.filter(movies_id=movies_id)
	season_details=Season_list.objects.filter(season_movies_id=movies_id)
	season_id_param=request.GET.get('season_id')
	episode_id_param=request.GET.get('episode_id')
	print(season_id_param)
	print(episode_id_param)
	episode_details=Episode_list.objects.filter(episode_season_id=season_id_param)
	# episode_details=Episode_list.objects.filter(episode_season_id__season_movies_id=movies_id)
	link_details=Link_list.objects.filter(link_episode_season_id__episode_season_id__season_movies_id=movies_id)
	context={
		"movies_details":movies_details,
		"season_details":season_details,
		"episode_details":episode_details,
		"season_id_param":season_id_param,
		"link_details":link_details

	}
	return render(request,"movies_list/movies_details.html",context)

def Genre_detail(request,genre_name):
	genre_details=Movies_list.objects.filter(genre__genre_name=genre_name)
	context={
		"genre_details":genre_details,
	}
	return render(request,"movies_list/genre_details.html",context)

def Cast_detail(request,cast_name):
	cast_details=Movies_list.objects.filter(cast__cast_name=cast_name)
	paginator = Paginator(cast_details, 4)
	page = request.GET.get('page')
	cast_details = paginator.get_page(page)
	print(cast_details.has_previous())
	print(cast_details.has_next())
	context={
		"cast_details":cast_details,
	}
	return render(request,"movies_list/cast_details.html",context)

def Director_detail(request,director_name):
	director_details=Movies_list.objects.filter(director__director_name=director_name)
	context={
		"director_details":director_details,
	}
	return render(request,"movies_list/director_details.html",context)
def Writer_detail(request,writer_name):
	writer_details=Movies_list.objects.filter(writer__writer_name=writer_name)
	context={
		"x":writer_details,
	}
	return render(request,"movies_list/writer_details.html",context)
def Award_detail(request,award_name):
	award_details=Movies_list.objects.filter(awards__award_name=award_name)
	context={
		"award_details":award_details,
	}
	return render(request,"movies_list/award_details.html",context)
def Country_detail(request,country_name):
	country_details=Movies_list.objects.filter(country__country_name=country_name)
	context={
		"country_details":country_details,
	}
	return render(request,"movies_list/country_details.html",context)
def Language_detail(request,language_name):
	language_details=Movies_list.objects.filter(language__language_name=language_name)
	context={
		"language_details":language_details,
	}
	return render(request,"movies_list/language_details.html",context)
def Movies_type_detail(request,movies_type_name):
	movies_type_details=Movies_list.objects.filter(movies_type__movies_type_name=movies_type_name)
	context={
		"movies_type_details":movies_type_details,
	}
	return render(request,"movies_list/movies_type_details.html",context)

def Quality_detail(request,quality_name):
	quality_details=Movies_list.objects.filter(Quality__quality_name=quality_name)
	context={
		"quality_details":quality_details,
	}
	return render(request,"movies_list/quality_details.html",context)


@login_required
def Contact_list(request):
	form=Create_Contact_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:8]
	if form.is_valid():
		if request.user.is_staff:
			obj = form.save(commit=False)
			obj.contact_user_id = request.user
			form.save()
			messages.success(request, f'Thank you for contacting with us!')
			return redirect('movies-index')
			
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url
	}   
	return render(request,'movies_list/contact.html',context)















@login_required
def Award_list_create(request):
	form=Create_Award_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:-5]
	if form.is_valid():
		if request.user.is_staff:
			form.save()
			messages.success(request, f'Award List has been created!')
			
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url
	}   
	return render(request,'movies_list/list_create.html',context)
@login_required
def Cast_list_create(request):
	form=Create_Cast_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:-5]
	
	
	if form.is_valid():
		if request.user.is_staff:
			form.save()
			messages.success(request, f'Cast List has been created!')
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url
	}   
	return render(request,'movies_list/list_create.html',context)

@login_required
def Director_list_create(request):
	form=Create_Director_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:-5]
	
	
	if form.is_valid():
		if request.user.is_staff:
			form.save()
			messages.success(request, f'Director List has been created!')
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url
	}   
	return render(request,'movies_list/list_create.html',context)
@login_required
def Writer_list_create(request):
	form=Create_Writer_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:-5]
	
	
	if form.is_valid():
		if request.user.is_staff:
			form.save()
			messages.success(request, f'Writer List has been created!')
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url
	}   
	return render(request,'movies_list/list_create.html',context)

@login_required
def Country_list_create(request):
	form=Create_Country_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:-5]
	
	
	if form.is_valid():
		if request.user.is_staff:
			form.save()
			messages.success(request, f'Country List has been created!')
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url
	}   
	return render(request,'movies_list/list_create.html',context)

@login_required
def Genre_list_create(request):
	form=Create_Genre_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:-5]
	if form.is_valid():
		if request.user.is_staff:
			form.save()
			messages.success(request, f'Genre List has been created!')
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url
	}   
	return render(request,'movies_list/list_create.html',context)

@login_required  
def Language_list_create(request):
	form=Create_Language_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:-5]
	
	
	if form.is_valid():
		if request.user.is_staff:
			form.save()
			messages.success(request, f'Language List has been created!')
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url
	}   
	return render(request,'movies_list/list_create.html',context)
@login_required
def Quality_list_create(request):
	form=Create_Quality_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:-5]
	
	
	if form.is_valid():
		if request.user.is_staff:
			form.save()
			messages.success(request, f'Quality List has been created!')
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url
	}   
	return render(request,'movies_list/list_create.html',context)

@login_required
def Server_list_create(request):
	form=Create_Server_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:-5]
	
	
	if form.is_valid():
		if request.user.is_staff:
			form.save()
			messages.success(request, f'Server List has been created!')
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url
	}   
	return render(request,'movies_list/list_create.html',context)
@login_required
def Content_type_list_create(request):
	form=Create_Content_type_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:-5]
	
	
	if form.is_valid():
		if request.user.is_staff:
			form.save()
			messages.success(request, f'server type List has been created!')
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url
	}   
	return render(request,'movies_list/list_create.html',context)
@login_required
def Subtitle_list_create(request):
	form=Create_Subtitle_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:-5]
	
	
	if form.is_valid():
		if request.user.is_staff:
			form.save()
			messages.success(request, f'subtitle List has been created!')
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url
	}   
	return render(request,'movies_list/list_create.html',context)

@login_required
def Movies_type_list_create(request):
	form=Create_Movies_type_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:-5]
	
	
	if form.is_valid():
		if request.user.is_staff:
			form.save()
			messages.success(request, f'Movies type List has been created!')
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url
	}   
	return render(request,'movies_list/list_create.html',context)

@login_required
def Movies_create(request):
	form=Create_Movies_form(
			data=(request.POST or None),
			files=(request.FILES or None),

		)
	url=request.path[1:-5]	
	if form.is_valid():
		if request.user.is_active:
			r=Movies_list.objects.create(
				name=request.POST["name"],
				country_id=request.POST["country"],
				story_line=request.POST["story_line"],
				cost=request.POST["cost"],
				release_date=request.POST["release_date"],
				imdb_rating=request.POST["imdb_rating"],
				imdb_link=request.POST["imdb_link"],
				trailer_link=request.POST["trailer_link"],
				Quality_id=request.POST["quality"],
				movies_type_id=request.POST["movies_type"],
				movies_thumbnail=request.FILES["movies_thumbnail"],
				movies_user_id_id=request.user.id,
				)
			
			s='cast_show_result'
			for i in range(10):
				x=f'{s}{i}'
				username = request.POST.get(f'{s}{i}')
				if username != None:
					print(username)
					r.cast.add(username)
			s='genre_show_result'
			for i in range(10):
				x=f'{s}{i}'
				username = request.POST.get(f'{s}{i}')
				if username != None:
					print(username)
					r.genre.add(username)
			s='director_show_result'
			for i in range(10):
				x=f'{s}{i}'
				username = request.POST.get(f'{s}{i}')
				if username != None:
					print(username)
					r.director.add(username)
			s='writer_show_result'
			for i in range(10):
				x=f'{s}{i}'
				username = request.POST.get(f'{s}{i}')
				if username != None:
					print(username)
					r.writer.add(username)
			s='award_show_result'
			for i in range(10):
				x=f'{s}{i}'
				username = request.POST.get(f'{s}{i}')
				if username != None:
					print(username)
					r.awards.add(username)
			s='language_show_result'
			for i in range(10):
				x=f'{s}{i}'
				username = request.POST.get(f'{s}{i}')
				if username != None:
					print(username)
					r.language.add(username)
			r.save()
			rp=Movies_list.objects.aggregate(Max('movies_id'))
			x=[*rp.values()][0]	
			messages.success(request, f'Movies has been created!')
			return redirect('movies-detail',x)
			
		else:
			messages.warning(request, f'Please Login to create movies!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url
	}   
	return render(request,'movies_list/movies_list_create.html',context)
def load_cast(request):
	text_input = request.GET.get('text_input')
	casts = Cast_list.objects.filter(cast_name__contains=text_input).order_by('cast_name')
	return render(request, 'movies_list/cast_dropdown_list_options.html', {'casts': casts})
def load_genre(request):
	text_input = request.GET.get('text_input')
	genres = Genre_list.objects.filter(genre_name__contains=text_input).order_by('genre_name')
	return render(request, 'movies_list/genre_dropdown_list_options.html', {'genres': genres})

def load_director(request):
	text_input = request.GET.get('text_input')
	directors = Director_list.objects.filter(director_name__contains=text_input).order_by('director_name')
	return render(request, 'movies_list/director_dropdown_list_options.html', {'directors': directors})


def load_writer(request):
	text_input = request.GET.get('text_input')
	writers = Writer_list.objects.filter(writer_name__contains=text_input).order_by('writer_name')
	return render(request, 'movies_list/writer_dropdown_list_options.html', {'writers': writers})
def load_award(request):
	text_input = request.GET.get('text_input')
	awards = Award_list.objects.filter(award_name__contains=text_input).order_by('award_name')
	return render(request, 'movies_list/award_dropdown_list_options.html', {'awards': awards})
def load_language(request):
	text_input = request.GET.get('text_input')
	languages = Language_list.objects.filter(language_name__contains=text_input).order_by('language_name')
	return render(request, 'movies_list/language_dropdown_list_options.html', {'languages': languages})




@login_required
def Season_create(request,movies_id):
	form=Create_Season_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:7]
	
	
	if form.is_valid():
		if request.user.is_active:
			# x=Movies_list.objects.filter(movies_id=1)
			# x=x[0]
			obj = form.save(commit=False)
			obj.season_user_id = request.user
			obj.season_movies_id_id=movies_id
			obj.save()
			form.save_m2m()
			messages.success(request, f'Season has been created!')
			return redirect('movies-detail',movies_id)
		else:
			messages.warning(request, f'Please Login to create movies!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url
	}   
	return render(request,'movies_list/list_create.html',context)


@login_required
def Episode_create(request,movies_id,season_id):
	form=Create_Episode_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:8]
	
	
	if form.is_valid():
		if request.user.is_active:
			# x=Season_list.objects.filter(season_id=1)
			# x=x[0]
			obj = form.save(commit=False)
			obj.episode_user_id = request.user
			obj.episode_season_id_id=season_id
			obj.save()
			form.save_m2m()
			messages.success(request, f'Season has been created!')
			return redirect('movies-detail',movies_id)
		else:
			messages.warning(request, f'Please Login to create movies!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url
	}   
	return render(request,'movies_list/list_create.html',context)


@login_required
def Link_create(request,movies_id,season_id,episode_id):
	form=Create_Link_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:5]
	
	
	if form.is_valid():
		if request.user.is_active:
			# x=Episode_list.objects.filter(episode_id=1)
			# x=x[0]
		

			r=Link_list.objects.create(
				name=request.POST["name"],
				link=request.POST["link"],
				quality_id=request.POST["quality"],
				link_type_id=request.POST["link_type"],
				link_user_id_id=request.user.id,
				link_episode_season_id_id=episode_id)
			s='subtitle_show_result'
			for i in range(10):
				x=f'{s}{i}'
				username = request.POST.get(f'{s}{i}')
				if username != None:
					print(username)
					r.subtitle.add(username)
			r.save()
			messages.success(request, f'Season has been created!')
			return redirect('movies-detail',movies_id)

		else:
			messages.warning(request, f'Please Login to create movies!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url,
		"movies_id":movies_id,
		"season_id":season_id,
		"episode_id":episode_id,
	}   
	return render(request,'movies_list/link_list_create.html',context)

def load_subtitle(request):
	text_input = request.GET.get('text_input')
	subtitles = Subtitle_list.objects.filter(subtitle_name__contains=text_input).order_by('subtitle_name')
	return render(request, 'movies_list/subtitle_dropdown_list_options.html', {'subtitles': subtitles})






















