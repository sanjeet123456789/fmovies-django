from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
class Award_list(models.Model):
	award_id=models.AutoField(primary_key=True)
	award_name=models.CharField(max_length=50,blank=False)
	award_image = models.ImageField(upload_to='award_pics',default='award.jpg', )

	def __str__(self):
		return f'{self.award_name} '
	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

		img = Image.open(self.award_image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.award_image.path)

	class Meta:
		verbose_name_plural = 'Award'
	

class Cast_list(models.Model):
	cast_id=models.AutoField(primary_key=True)
	cast_name=models.CharField(max_length=50)
	cast_image=models.ImageField(default='cast.jpg',upload_to='cast_pics')
	# role=models.CharField(max_length=40,default=None)
	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		img=Image.open(self.cast_image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.cast_image.path)

	def __str__(self):
		return f'{self.cast_name}'
	class Meta:
		verbose_name_plural='Cast'

class Director_list(models.Model):
	director_id=models.AutoField(primary_key=True)
	director_name=models.CharField(max_length=50)
	director_image=models.ImageField(default='cast.jpg',upload_to='director_pics')
	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		img=Image.open(self.director_image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.director_image.path)

	def __str__(self):
		return f'{self.director_name}'
	class Meta:
		verbose_name_plural='Director'

class Writer_list(models.Model):
	writer_id=models.AutoField(primary_key=True)
	writer_name=models.CharField(max_length=50);
	writer_image=models.ImageField(default='writer.jpg',upload_to='writer_pics')
	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		img=Image.open(self.writer_image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.writer_image.path)

	def __str__(self):
		return f'{self.writer_name}'
	class Meta:
		verbose_name_plural='Writer'


class Country_list(models.Model):
	country_id=models.AutoField(primary_key=True)
	country_name=models.CharField(max_length=50)
	country_short_code=models.CharField(max_length=5)
	country_image=models.ImageField(default='country.jpg',upload_to='country_pics')
	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		img=Image.open(self.country_image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.country_image.path)

	def __str__(self):
		return f'{self.country_name}'
	class Meta:
		verbose_name_plural='Country'

class Genre_list(models.Model):
	genre_id=models.AutoField(primary_key=True)
	genre_name=models.CharField(max_length=40)
	genre_image=models.ImageField(default='genre.jpg',upload_to='genre_pics')

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		img=Image.open(self.genre_image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.genre_image.path)

	def __str__(self):
		return f'{self.genre_name}'
	class Meta:
		verbose_name_plural='Genre'

class Language_list(models.Model):
	language_id=models.AutoField(primary_key=True)
	language_name=models.CharField(max_length=60)
	language_short_code=models.CharField(max_length=5)


	def __str__(self):
		return f'{self.language_name}'
	class Meta:
		verbose_name_plural='Language'


class Quality_list(models.Model):
	quality_id=models.AutoField(primary_key=True)
	quality_name=models.CharField(max_length=50)
	quality_priority=models.PositiveIntegerField()

	def __str__(self):
		return f'{self.quality_name}'
	class Meta:
		verbose_name_plural='Quality'

class Server_list(models.Model):
	server_id=models.AutoField(primary_key=True)
	server_name=models.CharField(max_length=50)
	
	def __str__(self):
		return f'{self.server_name}'
	class Meta:
		verbose_name_plural='Server_name'
class Content_type_list(models.Model):
	server_type_id=models.AutoField(primary_key=True)
	content_type=models.CharField(max_length=40)

	def __str__(self):
		return f'{ self.content_type}'
	class Meta:
		verbose_name_plural='content_type'

class Subtitle_list(models.Model):
	subtitle_id=models.AutoField(primary_key=True)
	subtitle_name=models.CharField(max_length=40)
	subtitle_short_code=models.CharField(max_length=5)
	def __str__(self):
		return f'{self.subtitle_name}'
	class Meta:
		verbose_name_plural="subtitle name"

class Movies_type_list(models.Model):
	movies_type_id=models.AutoField(primary_key=True)
	movies_type_name=models.CharField(max_length=12)
	def __str__(self):
		return f'{self.movies_type_name}'
	class Meta:
		verbose_name_plural='movies_type'

class Movies_list(models.Model):
	movies_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	genre=models.ManyToManyField(Genre_list)
	cast=models.ManyToManyField(Cast_list)
	director=models.ManyToManyField(Director_list)
	writer=models.ManyToManyField(Writer_list)
	awards=models.ManyToManyField(Award_list)
	country=models.ForeignKey(Country_list, on_delete=models.PROTECT)
	story_line=models.TextField(default='')
	cost=models.PositiveIntegerField(default=0)
	release_date=models.DateTimeField( blank=False,null=False)
	created_at=models.DateTimeField(default=timezone.now)
	language=models.ManyToManyField(Language_list)
	imdb_rating=models.FloatField()
	imdb_link=models.TextField()
	trailer_link=models.TextField()
	views=models.PositiveIntegerField(default=0)
	likes=models.PositiveIntegerField(default=0)
	dislike=models.PositiveIntegerField(default=0)
	ratting=models.FloatField(default=0.0)
	tags=models.TextField()
	Quality=models.ForeignKey(Quality_list,on_delete=models.PROTECT)
	movies_user_id=models.ForeignKey(User, on_delete=models.PROTECT)
	movies_type=models.ForeignKey(Movies_type_list,on_delete=models.PROTECT)
	movies_thumbnail=models.ImageField(default='thumbnail.jpg',upload_to='movies_pics')

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		img=Image.open(self.movies_thumbnail.path)
		if img.height > 100 or img.width > 100:
			output_size = (200,300)
			image_movies=img.resize(output_size,resample=Image.ANTIALIAS)
			image_movies.save(self.movies_thumbnail.path)
	

	def __str__(self):
		return f'{self.movies_id}'
	class Meta:
		verbose_name_plural='movies'

class Season_list(models.Model):
	season_id=models.AutoField(primary_key=True)
	season_movies_id=models.ForeignKey(Movies_list, on_delete=models.CASCADE)
	season_no=models.PositiveIntegerField()
	season_name=models.CharField(max_length=50)
	season_desc=models.TextField()
	season_user_id=models.ForeignKey(User, on_delete=models.PROTECT)
	def __str__(self):
		return f'{self.season_name}'
	class Meta:
		verbose_name_plural='Season'

class Episode_list(models.Model):
	episode_id=models.AutoField(primary_key=True)
	episode_season_id=models.ForeignKey(Season_list, on_delete=models.CASCADE)
	episode_user_id=models.ForeignKey(User, on_delete=models.PROTECT)
	name=models.CharField(max_length=50)
	adult=models.BooleanField(default=False)
	filler=models.BooleanField(default=False)
	desc=models.TextField()
	episode_views=models.PositiveIntegerField(default=0)
	episode_like=models.PositiveIntegerField(default=0)
	episode_dislike=models.PositiveIntegerField(default=0)
	def __str__(self):
		return f'{self.name}'
	class Meta:
		verbose_name_plural='Episode'

class Link_list(models.Model):
	link_id=models.AutoField(primary_key=True)
	link_episode_season_id=models.ForeignKey(Episode_list,on_delete=models.PROTECT)
	link_user_id=models.ForeignKey(User, on_delete=models.PROTECT,blank=True)
	name=models.CharField(max_length=50)
	link=models.TextField()
	upvote=models.PositiveIntegerField(default=0)
	downvote=models.PositiveIntegerField(default=0)
	views=models.PositiveIntegerField(default=0)
	link_type=models.ForeignKey(Content_type_list,on_delete=models.PROTECT)
	subtitle=models.ManyToManyField(Subtitle_list)
	link_created_at=models.DateTimeField(default=timezone.now)
	quality=models.ForeignKey(Quality_list,on_delete=models.PROTECT)

	# def __str__(self):
	# 	return f'{self.name}'
	class Meta:
		verbose_name_plural='Link'







class Contact(models.Model):
	msg_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	contact_user_id=models.ForeignKey(User, on_delete=models.PROTECT,blank=True)
	email=models.CharField(max_length=50,default="")
	message=models.TextField(default="")
	phone=models.CharField(max_length=50)
	screenshot=models.ImageField(upload_to='contact_pics',blank=True)

	






































