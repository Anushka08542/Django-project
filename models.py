from django.db import models

# Create your models here.
class Logs(models.Model):
	name=models.CharField(max_length=264,unique=True)
	email=models.EmailField(unique=True)
	password=models.CharField(max_length=264)
