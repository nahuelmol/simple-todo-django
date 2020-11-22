from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime

def hours_ahead(req,post_id):
	random_integer = int(post_id)
	dt = datetime.datetime.now() 

	context = {'date':dt,'ram':random_integer}
	
	return render(req,'date.html',context)