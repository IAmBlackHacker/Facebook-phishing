from django.db import models

# Create your models here.
class passwords(models.Model):
	username=models.CharField(max_length=100,null=True)
	password=models.CharField(max_length=100,null=True)
	def __str__(self):
		return self.username
