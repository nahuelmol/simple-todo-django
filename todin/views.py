from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import itemModel

def seeing_view(request):
	all_items = itemModel.objects.all() 
	return render(request,'todo.html', {'itemalls': all_items})


def adding_data(request):
	f = request.POST['first_name']
	l = request.POST['last_name']

	new_item = itemModel(myname = f )
	new_item.save()

	second_item = itemModel(last_n = l)
	second_item.save()

	return HttpResponseRedirect('/todo/')