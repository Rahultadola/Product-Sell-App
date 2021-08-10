from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	title       	= models.CharField(max_length=120)
	description 	= models.TextField(blank=True, null=True)
	descrip_image 	= models.ImageField(upload_to='static/products', null=True)
	price      		= models.DecimalField(decimal_places=2, max_digits=10000)
	sold			= models.IntegerField(default=0)
	featured		= models.BooleanField(null=False, default=True)
	user			= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	date_register	= models.DateField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse("products:product-detail", kwargs={"id": self.id})

	def __str__(self):
		return f'{self.title}'
