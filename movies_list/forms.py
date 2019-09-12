from django import forms
from movies_list.models import *

class Create_Award_list_form(forms.ModelForm):
    class Meta:
        model=Award_list
        fields=['award_name','award_image']

class Create_Cast_list_form(forms.ModelForm):
	class Meta:
		model=Cast_list
		fields=['cast_name','cast_image']

class Create_Director_list_form(forms.ModelForm):
	class Meta:
		model=Director_list
		fields=['director_name','director_image']

class Create_Writer_list_form(forms.ModelForm):
	class Meta:
		model=Writer_list
		fields=['writer_name','writer_image']

class Create_Country_list_form(forms.ModelForm):
	class Meta:
		model=Country_list
		fields=['country_name','country_short_code','country_image']

class Create_Genre_list_form(forms.ModelForm):
	class Meta:
		model=Genre_list
		fields=['genre_name','genre_image']

class Create_Language_list_form(forms.ModelForm):
	class Meta:
		model=Language_list
		fields=['language_name','language_short_code']
		
class Create_Quality_list_form(forms.ModelForm):
	class Meta:
		model=Quality_list
		fields=['quality_name','quality_priority']
		
class Create_Server_list_form(forms.ModelForm):
	class Meta:
		model=Server_list
		fields=['server_name']
		
class Create_Content_type_list_form(forms.ModelForm):
	class Meta:
		model=Content_type_list
		fields=['content_type']
		
class Create_Subtitle_list_form(forms.ModelForm):
	class Meta:
		model=Subtitle_list
		fields=['subtitle_name','subtitle_short_code']
		
class Create_Movies_type_list_form(forms.ModelForm):
	class Meta:
		model=Movies_type_list
		fields=['movies_type_name']
		
class Create_Movies_form(forms.ModelForm):
	class Meta:
		model=Movies_list
		fields=['name','genre','cast','director','writer','awards','country','story_line','cost','release_date','created_at','language','imdb_rating','imdb_link','trailer_link','tags','Quality','movies_type',]

class Create_Season_form(forms.ModelForm):
	class Meta:
		model=Season_list
		fields=['season_no','season_name','season_desc']
class Create_Episode_form(forms.ModelForm):
	class Meta:
		model=Episode_list
		fields=['name','adult','filler','desc',]

class Create_Link_form(forms.ModelForm):
	class Meta:
		model=Link_list
		fields=['name','link','link_type','subtitle','quality']