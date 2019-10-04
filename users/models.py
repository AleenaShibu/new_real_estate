from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	TYPE = [
			('seller'),
			('buyer'),
			

		]
	age = models.PositiveIntegerField(null=True, blank=True)





