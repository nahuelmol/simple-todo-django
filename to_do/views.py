from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def main_init(req):
	
	return render(req,'index.html')
