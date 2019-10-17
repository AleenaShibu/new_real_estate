from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	TYPE = [
			('Seller','seller'),
			('Buyer','buyer'),
			

		]
	
	category= models.CharField(max_length=40,choices=TYPE)
	mobile_number=models.CharField(max_length=10,blank=True)





