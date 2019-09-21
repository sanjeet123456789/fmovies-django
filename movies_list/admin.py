from django.contrib import admin
from . forms import Update_Movies_form
from . models import (Award_list,
	Cast_list,
	Director_list,
	Writer_list,
	Country_list,
	Genre_list,
	Language_list,
	Quality_list,
	Server_list,
	Content_type_list,
	Subtitle_list,
	Movies_type_list,
	Movies_list,
	Season_list,
	Episode_list,
	Link_list,
	Contact


	)
admin.site.register(Award_list)
admin.site.register(Cast_list)
admin.site.register(Director_list)
admin.site.register(Writer_list)
admin.site.register(Country_list)
admin.site.register(Genre_list)
admin.site.register(Language_list)
admin.site.register(Quality_list)
admin.site.register(Server_list)
admin.site.register(Content_type_list)
admin.site.register(Subtitle_list)
admin.site.register(Movies_type_list)
admin.site.register(Movies_list)
admin.site.register(Season_list)
admin.site.register(Episode_list)
admin.site.register(Link_list)
admin.site.register(Contact)

