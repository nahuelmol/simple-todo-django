from django.db import models

class itemModel(models.Model):
	first_name = models.TextField()
	last_name = models.TextField()
	age = models.IntegerField(default=0)
	username = models.TextField()
	post = models.TextField()