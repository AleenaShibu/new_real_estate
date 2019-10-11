from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model



class Realtor(models.Model):
  bedroom_choices = {
  				'1':1,
  				'2':2,
  				'3':3,
  				'4':4,
  				'5':5,
   					}
  price_choices = {
  				'100000':'$100,000',
  				'200000':'$200,000',
  				'300000':'$300,000',
  				'400000':'$400,000',
  
					}
  
  District_choices = {

        		'TVM' : 'Thiruvananthapuram', 
        		'ALP' :	'Alappuzha', 
        
        		'KTM' :	'Kottayam', 
        		'IDK' :	'Idukki', 
        		'ERKLM'	:'Ernakulam,'
        		
       				}
  class Meta:
    verbose_name = 'Realtor'


  owner_name = models.CharField(max_length=200)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  description = models.TextField(blank=True)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  district = models.TextField(blank =True)
  price = models.PositiveIntegerField(default=100000)
  created_date = models.DateTimeField(auto_now_add=True,editable=False,blank=False,null=False)
  owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
	
  def __str__(self):
    return self.owner
	
  def get_absolute_url(self):
    return reverse('detail', args=[str(self.id)])	

# for comments
class Comment(models.Model):
  post = models.ForeignKey('realtors.Realtor', on_delete=models.CASCADE, related_name='comments')
  user = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True,editable=False,blank=False,null=False)
  approved_comment = models.BooleanField(default=False)

  def approve(self):
    self.approved_comment = True
    self.save()

  def __str__(self):
    return self.text

    
 
 