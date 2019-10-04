from django.db import models

class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_name = models.TextField()
    place = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    
    owner_name = models.TextField(blank=True)
   
    def __str__(self):
        return self.name
