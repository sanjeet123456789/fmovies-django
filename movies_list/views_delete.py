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
def Award_list_delete(request,award_id):
	obj=get_object_or_404(Award_list,award_id=award_id)
	url=url_filter(request,award_id)
	form=Create_Award_list_form(
			instance=obj,
		)
	if request.method=="POST":
		if request.user.is_superuser: 
			obj.delete()
			messages.success(request, f''+url+' '+str(award_id)+' has been deleted!')
			return redirect('movies-index')
		else:
			messages.warning(request, f'You do not have Admin access!')
	context={
		"obj":obj,
		"form":form,
		"form_name":url,
	}
	return render(request,"movies_list/list_delete.html",context)


@login_required
def Cast_list_delete(request,cast_id):
	obj_cast=get_object_or_404(Cast_list,cast_id=cast_id)
	url=url_filter(request,cast_id)
	form=Create_Cast_list_form(
			instance=obj_cast,
		)
	if request.method=="POST":
		if request.user.is_superuser: 
			obj.delete()
			messages.success(request, f''+url+' '+str(cast_id)+' has been deleted!')
			return redirect('movies-index')
		else:
			messages.warning(request, f'You do not have Admin access!')
	context={
		"obj":obj_cast,
		"form":form,
		"form_name":url,
	}
	return render(request,"movies_list/list_delete.html",context)






@login_required
def Director_list_delete(request,director_id):
	obj=get_object_or_404(Director_list,director_id=director_id)
	url=url_filter(request,director_id)
	form=Create_Director_list_form(
			instance=obj,
		)
	if request.method=="POST":
		if request.user.is_superuser: 
			obj.delete()
			messages.success(request, f''+url+' '+str(director_id)+' has been deleted!')
			return redirect('movies-index')
		else:
			messages.warning(request, f'You do not have Admin access!')
	context={
		"obj":obj,
		"form":form,
		"form_name":url,
	}
	return render(request,"movies_list/list_delete.html",context)


@login_required
def Writer_list_delete(request,writer_id):
	obj=get_object_or_404(Writer_list,writer_id=writer_id)
	url=url_filter(request,writer_id)
	form=Create_Writer_list_form(
			instance=obj,
		)
	if request.method=="POST":
		if request.user.is_superuser: 
			obj.delete()
			messages.success(request, f''+url+' '+str(writer_id)+' has been deleted!')
			return redirect('movies-index')
		else:
			messages.warning(request, f'You do not have Admin access!')
	context={
		"obj":obj,
		"form":form,
		"form_name":url,
	}
	return render(request,"movies_list/list_delete.html",context)




@login_required
def Country_list_delete(request,country_id):
	obj=get_object_or_404(Country_list,country_id=country_id)
	url=url_filter(request,country_id)
	form=Create_Country_list_form(
			instance=obj,
		)
	if request.method=="POST":
		if request.user.is_superuser: 
			obj.delete()
			messages.success(request, f''+url+' '+str(country_id)+' has been deleted!')
			return redirect('movies-index')
		else:
			messages.warning(request, f'You do not have Admin access!')
	context={
		"obj":obj,
		"form":form,
		"form_name":url,
	}
	return render(request,"movies_list/list_delete.html",context)

@login_required
def Quality_list_delete(request,quality_id):
	obj=get_object_or_404(Quality_list,quality_id=quality_id)
	url=url_filter(request,quality_id)
	form=Create_Quality_list_form(
			instance=obj,
		)
	if request.method=="POST":
		if request.user.is_superuser: 
			obj.delete()
			messages.success(request, f''+url+' '+str(quality_id)+' has been deleted!')
			return redirect('movies-index')
		else:
			messages.warning(request, f'You do not have Admin access!')
	context={
		"obj":obj,
		"form":form,
		"form_name":url,
	}
	return render(request,"movies_list/list_delete.html",context)

@login_required
def Genre_list_delete(request,genre_id):
	obj=get_object_or_404(Genre_list,genre_id=genre_id)
	url=url_filter(request,genre_id)
	form=Create_Genre_list_form(
			instance=obj,
		)
	if request.method=="POST":
		if request.user.is_superuser: 
			obj.delete()
			messages.success(request, f''+url+' '+str(genre_id)+' has been deleted!')
			return redirect('movies-index')
		else:
			messages.warning(request, f'You do not have Admin access!')
	context={
		"obj":obj,
		"form":form,
		"form_name":url,
	}
	return render(request,"movies_list/list_delete.html",context)

@login_required
def Language_list_delete(request,language_id):
	obj=get_object_or_404(Language_list,language_id=language_id)
	url=url_filter(request,language_id)
	form=Create_Language_list_form(
			instance=obj,
		)
	if request.method=="POST":
		if request.user.is_superuser: 
			obj.delete()
			messages.success(request, f''+url+' '+str(language_id)+' has been deleted!')
			return redirect('movies-index')
		else:
			messages.warning(request, f'You do not have Admin access!')
	context={
		"obj":obj,
		"form":form,
		"form_name":url,
	}
	return render(request,"movies_list/list_delete.html",context)
@login_required
def Server_list_delete(request,server_id):
	obj=get_object_or_404(Server_list,server_id=server_id)
	url=url_filter(request,server_id)
	form=Create_Server_list_form(
			instance=obj,
		)
	if request.method=="POST":
		if request.user.is_superuser: 
			obj.delete()
			messages.success(request, f''+url+' '+str(server_id)+' has been deleted!')
			return redirect('movies-index')
		else:
			messages.warning(request, f'You do not have Admin access!')
	context={
		"obj":obj,
		"form":form,
		"form_name":url,
	}
	return render(request,"movies_list/list_delete.html",context)
@login_required
def Content_type_list_delete(request,server_type_id):
	obj=get_object_or_404(Content_type_list,server_type_id=server_type_id)
	url=url_filter(request,server_type_id)
	form=Create_Content_type_list_form(
			instance=obj,
		)
	if request.method=="POST":
		if request.user.is_superuser: 
			obj.delete()
			messages.success(request, f''+url+' '+str(server_type_id)+' has been deleted!')
			return redirect('movies-index')
		else:
			messages.warning(request, f'You do not have Admin access!')
	context={
		"obj":obj,
		"form":form,
		"form_name":url,
	}
	return render(request,"movies_list/list_delete.html",context)
@login_required
def Subtitle_list_delete(request,subtitle_id):
	obj=get_object_or_404(Subtitle_list,subtitle_id=subtitle_id)
	url=url_filter(request,subtitle_id)
	form=Create_Subtitle_list_form(
			instance=obj,
		)
	if request.method=="POST":
		if request.user.is_superuser: 
			obj.delete()
			messages.success(request, f''+url+' '+str(subtitle_id)+' has been deleted!')
			return redirect('movies-index')
		else:
			messages.warning(request, f'You do not have Admin access!')
	context={
		"obj":obj,
		"form":form,
		"form_name":url,
	}
	return render(request,"movies_list/list_delete.html",context)
@login_required
def Movies_type_list_delete(request,movies_type_id):
	obj=get_object_or_404(Movies_type_list,movies_type_id=movies_type_id)
	url=url_filter(request,movies_type_id)
	form=Create_Subtitle_list_form(
			instance=obj,
		)
	if request.method=="POST":
		if request.user.is_superuser: 
			obj.delete()
			messages.success(request, f''+url+' '+str(movies_type_id)+' has been deleted!')
			return redirect('movies-index')
		else:
			messages.warning(request, f'You do not have Admin access!')
	context={
		"obj":obj,
		"form":form,
		"form_name":url,
	}
	return render(request,"movies_list/list_delete.html",context)

@login_required
def Movies_delete(request,movies_id):
	obj=get_object_or_404(Movies_list,movies_id=movies_id)
	url=url_filter(request,movies_id)
	form=Create_Movies_form(
			instance=obj,
		)
	if request.method=="POST":
		if request.user.is_superuser: 
			obj.delete()
			messages.success(request, f''+url+' '+str(movies_id)+' has been deleted!')
			return redirect('movies-index')
		else:
			messages.warning(request, f'You do not have Admin access!')
	context={
		"obj":obj,
		"form":form,
		"form_name":url,
	}
	return render(request,"movies_list/list_delete.html",context)

@login_required
def Season_delete(request,season_id):
	obj=get_object_or_404(Season_list,season_id=season_id)
	url=url_filter(request,season_id)
	form=Create_Season_form(
			instance=obj,
		)
	if request.method=="POST":
		if request.user.is_superuser: 
			obj.delete()
			messages.success(request, f''+url+' '+str(season_id)+' has been deleted!')
			return redirect('movies-index')
		else:
			messages.warning(request, f'You do not have Admin access!')
	context={
		"obj":obj,
		"form":form,
		"form_name":url,
	}
	return render(request,"movies_list/list_delete.html",context)
@login_required
def Episode_delete(request,episode_id):
	obj=get_object_or_404(Episode_list,episode_id=episode_id)
	url=url_filter(request,episode_id)
	form=Create_Episode_form(
			instance=obj,
		)
	if request.method=="POST":
		if request.user.is_superuser: 
			obj.delete()
			messages.success(request, f''+url+' '+str(episode_id)+' has been deleted!')
			return redirect('movies-index')
		else:
			messages.warning(request, f'You do not have Admin access!')
	context={
		"obj":obj,
		"form":form,
		"form_name":url,
	}
	return render(request,"movies_list/list_delete.html",context)
@login_required
def Link_delete(request,link_id):
	obj=get_object_or_404(Link_list,link_id=link_id)
	url=url_filter(request,link_id)
	form=Create_Link_form(
			instance=obj,
		)
	if request.method=="POST":
		if request.user.is_superuser: 
			obj.delete()
			messages.success(request, f''+url+' '+str(link_id)+' has been deleted!')
			return redirect('movies-index')
		else:
			messages.warning(request, f'You do not have Admin access!')
	context={
		"obj":obj,
		"form":form,
		"form_name":url,
	}
	return render(request,"movies_list/list_delete.html",context)

