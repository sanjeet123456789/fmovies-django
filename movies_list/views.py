from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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

def Movies_detail(request,movies_id):
	movies_details=Movies_list.objects.filter(movies_id=movies_id)
	# Movies_list.objects.filter(cast__pk=1) reverse reference
	genre_movies_details=Genre_list.objects.filter(movies_list__movies_id=movies_id)
	cast_movies_details=Cast_list.objects.filter(movies_list__movies_id=movies_id)
	director_movies_details=Director_list.objects.filter(movies_list__movies_id=movies_id)

	writer_movies_details=Writer_list.objects.filter(movies_list__movies_id=movies_id)
	awards_movies_details=Award_list.objects.filter(movies_list__movies_id=movies_id)
	country_movies_details=Country_list.objects.filter(movies_list__movies_id=movies_id)
	movies_type_movies_details=Movies_type_list.objects.filter(movies_list__movies_id=movies_id)
	movies_user_id_movies_details=User.objects.filter(movies_list__movies_id=movies_id)
	language_movies_details=Language_list.objects.filter(movies_list__movies_id=movies_id)
	quality_movies_details=Quality_list.objects.filter(movies_list__movies_id=movies_id)#only for manytoone and manytomany relations
	
	context={
		"movies_details":movies_details,
		"genre_movies_details":genre_movies_details,
		"director_movies_details":director_movies_details,
		"cast_movies_details":cast_movies_details,
		"writer_movies_details":writer_movies_details,
		"awards_movies_details":awards_movies_details,
		"country_movies_details":country_movies_details,
		"movies_type_movies_details":movies_type_movies_details,
		"language_movies_details":language_movies_details,
		"movies_user_id_movies_details":movies_user_id_movies_details,
		"quality_movies_details":quality_movies_details
	}
	return render(request,"movies_list/movies_details.html",context)

























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
			obj = form.save(commit=False)
			obj.movies_user_id = request.user
			obj.save()
			messages.success(request, f'Movies has been created!')
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
def Season_create(request):
	form=Create_Season_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:-5]
	
	
	if form.is_valid():
		if request.user.is_active:
			x=Movies_list.objects.filter(movies_id=1)
			x=x[0]
			obj = form.save(commit=False)
			obj.season_user_id = request.user
			obj.season_movies_id=x
			obj.save()
			messages.success(request, f'Season has been created!')
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
def Episode_create(request):
	form=Create_Episode_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:-5]
	
	
	if form.is_valid():
		if request.user.is_active:
			x=Season_list.objects.filter(season_id=1)
			x=x[0]
			obj = form.save(commit=False)
			obj.episode_user_id = request.user
			obj.episode_season_id=x
			obj.save()
			messages.success(request, f'Season has been created!')
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
def Link_create(request):
	form=Create_Link_form(
			data=(request.POST or None),
			files=(request.FILES or None),
		)
	url=request.path[1:-5]
	
	
	if form.is_valid():
		if request.user.is_active:
			x=Episode_list.objects.filter(episode_id=1)
			x=x[0]
			obj = form.save(commit=False)
			obj.link_user_id = request.user
			obj.link_episode_season_id=x
			obj.save()
			messages.success(request, f'Season has been created!')
		else:
			messages.warning(request, f'Please Login to create movies!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url
	}   
	return render(request,'movies_list/list_create.html',context)