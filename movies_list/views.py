from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Max

from django.views.generic import(
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView


	)
from .models import Award_list
from .forms import *
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