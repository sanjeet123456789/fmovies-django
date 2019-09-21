from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Max
from .forms import *
from .models import *








def url_filter(request,x):
	if x<10:
		url=request.path[1:-9]
	elif x<100:
		url=request.path[1:-10]
	elif x<1000:
		url=request.path[1:-11]
	else:
		url=request.path[1:-12]
	return url

	
@login_required
def Award_list_update(request,award_id):
	obj=get_object_or_404(Award_list,award_id=award_id)
	url=url_filter(request,award_id)
	form=Create_Award_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
			instance=obj,
		)
	if form.is_valid():
		if request.user.is_staff:
			messages.success(request, f''+url+' List has been updated!')
			form.save()
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
	"form":form,
	"form_name":url,
	}
	return render(request,'movies_list/list_create.html',context)
	
@login_required
def Cast_list_update(request,cast_id):
	obj=get_object_or_404(Cast_list,cast_id=cast_id)
	form=Create_Cast_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
			instance=obj,
		)
	url=url_filter(request,cast_id)
	if form.is_valid():
		form.save()
		if request.user.is_staff:
			messages.success(request, f'Cast List has been updated!')
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url,
		}
	return render(request,'movies_list/list_create.html',context)
@login_required
def Director_list_update(request,director_id):
	obj=get_object_or_404(Director_list,director_id=director_id)
	form=Create_Director_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
			instance=obj,
		)
	url=url_filter(request,director_id)
	if form.is_valid():
		if request.user.is_staff:
			messages.success(request, f'Director List has been updated!')
			form.save()
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url,
		}
	return render(request,'movies_list/list_create.html',context)
@login_required
def Writer_list_update(request,writer_id):
	obj=get_object_or_404(Writer_list,writer_id=writer_id)
	form=Create_Writer_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
			instance=obj,
		)
	url=url_filter(request,writer_id)
	if form.is_valid():
		if request.user.is_staff:
			messages.success(request, f'Writer List has been updated!')
			form.save()
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url,
		}
	return render(request,'movies_list/list_create.html',context)
@login_required
def Country_list_update(request,country_id):
	obj=get_object_or_404(Country_list,country_id=country_id)
	form=Create_Country_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
			instance=obj,
		)
	url=url_filter(request,country_id)
	if form.is_valid():
		if request.user.is_staff:
			messages.success(request, f'Country List has been updated!')
			form.save()
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url,
		}
	return render(request,'movies_list/list_create.html',context)

@login_required
def Quality_list_update(request,quality_id):
	obj=get_object_or_404(Quality_list,quality_id=quality_id)
	form=Create_Quality_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
			instance=obj,
		)
	url=url_filter(request,quality_id)
	if form.is_valid():
		if request.user.is_staff:
			messages.success(request, f'Quality List has been updated!')
			form.save()
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url,
		}
	return render(request,'movies_list/list_create.html',context)

@login_required
def Genre_list_update(request,genre_id):
	obj=get_object_or_404(Genre_list,genre_id=genre_id)
	form=Create_Genre_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
			instance=obj,
		)
	url=url_filter(request,genre_id)
	if form.is_valid():
		if request.user.is_staff:
			messages.success(request, f'Quality List has been updated!')
			form.save()
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url,
		}
	return render(request,'movies_list/list_create.html',context)
@login_required
def Language_list_update(request,language_id):
	obj=get_object_or_404(Language_list,language_id=language_id)
	form=Create_Language_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
			instance=obj,
		)
	url=url_filter(request,language_id)
	if form.is_valid():
		if request.user.is_staff:
			messages.success(request, f'Language List has been updated!')
			form.save()
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url,
		}
	return render(request,'movies_list/list_create.html',context)
@login_required
def Server_list_update(request,server_id):
	obj=get_object_or_404(Server_list,server_id=server_id)
	form=Create_Server_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
			instance=obj,
		)
	url=url_filter(request,server_id)
	if form.is_valid():
		if request.user.is_staff:
			messages.success(request, f'Server List has been updated!')
			form.save()
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url,
		}
	return render(request,'movies_list/list_create.html',context)
@login_required
def Content_type_list_update(request,server_type_id):
	obj=get_object_or_404(Content_type_list,server_type_id=server_type_id)
	form=Create_Content_type_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
			instance=obj,
		)
	url=url_filter(request,server_type_id)
	if form.is_valid():
		if request.user.is_staff:
			messages.success(request, f'Content type List has been updated!')
			form.save()
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url,
		}
	return render(request,'movies_list/list_create.html',context)
@login_required
def Subtitle_list_update(request,subtitle_id):
	obj=get_object_or_404(Subtitle_list,subtitle_id=subtitle_id)
	form=Create_Subtitle_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
			instance=obj,
		)
	url=url_filter(request,subtile_id)
	if form.is_valid():
		if request.user.is_staff:
			messages.success(request, f'Subtitle List has been updated!')
			form.save()
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url,
		}
	return render(request,'movies_list/list_create.html',context)

@login_required
def Movies_type_list_update(request,movies_type_id):
	obj=get_object_or_404(Movies_type_list,movies_type_id=movies_type_id)
	form=Create_Movies_type_list_form(
			data=(request.POST or None),
			files=(request.FILES or None),
			instance=obj,
		)
	url=url_filter(request,movies_type_id)
	if form.is_valid():
		if request.user.is_staff:
			messages.success(request, f'Movies type List has been updated!')
			form.save()
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url,
		}
	return render(request,'movies_list/list_create.html',context)

@login_required
def Movies_update(request,movies_id):
	obj=get_object_or_404(Movies_list,movies_id=movies_id)
	form=Update_Movies_form(
			data=(request.POST or None),
			files=(request.FILES or None),
			instance=obj
		)
	url=url_filter(request,movies_id)
	if form.is_valid():
		if request.user.is_staff:
			messages.success(request, f'Movies type List has been updated!')
			form.save()
			return redirect('movies-detail',movies_id)
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url,
		}
	return render(request,'movies_list/list_create.html',context)
@login_required
def Season_update(request,season_id):
	obj=get_object_or_404(Season_list,season_id=season_id)
	form=Create_Season_form(
			data=(request.POST or None),
			files=(request.FILES or None),
			instance=obj,
		)
	url=url_filter(request,season_id)
	if form.is_valid():
		if request.user.is_staff:
			messages.success(request, f'Movies type List has been updated!')
			form.save()
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url,
		}
	return render(request,'movies_list/list_create.html',context)
@login_required
def Episode_update(request,episode_id):
	obj=get_object_or_404(Episode_list,episode_id=episode_id)
	form=Create_Episode_form(
			data=(request.POST or None),
			files=(request.FILES or None),
			instance=obj,
		)
	url=url_filter(request,episode_id)
	if form.is_valid():
		if request.user.is_staff:
			messages.success(request, f'Movies type List has been updated!')
			form.save()
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url,
		}
	return render(request,'movies_list/list_create.html',context)

@login_required
def Link_update(request,link_id):
	obj=get_object_or_404(Link_list,link_id=link_id)
	form=Create_Link_form(
			data=(request.POST or None),
			files=(request.FILES or None),
			instance=obj,
		)
	url=url_filter(request,link_id)
	if form.is_valid():
		if request.user.is_staff:
			messages.success(request, f'Movies type List has been updated!')
			form.save()
		else:
			messages.warning(request, f'You do not have Admin access!')
	else:
		print(form.errors)
	context={
		"form":form,
		"form_name":url,
		}
	return render(request,'movies_list/list_create.html',context)
