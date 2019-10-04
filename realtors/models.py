from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model



class Realtor(models.Model):
	name = models.CharField(max_length=200)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
	description = models.TextField(blank=True)
	phone = models.CharField(max_length=20)
	email = models.CharField(max_length=50)

	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('subject', args=[str(self.id)])	




 
 