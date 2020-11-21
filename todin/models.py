from django.db import models

class itemModel(models.Model):
	myname = models.TextField()
	last_n = models.TextField()