from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import itemModel

def seeing_view(request):
	all_items = itemModel.objects.all() 
	context = {'itemalls': all_items}
	return render(request,'todo.html',context)


def adding_data(request):
	f = request.POST['first_name']
	l = request.POST['last_name']
	myage = request.POST['age']
	user = request.POST['user']
	posts = request.POST['post']

	f_name = itemModel(first_name = f)
	l_name = itemModel(last_name = l)
	ages = itemModel(age = myage)
	username = itemModel(username=user)
	posts = itemModel(post = posts)

	f_name.save()
	l_name.save()
	ages.save()
	username.save()
	posts.save()

	return HttpResponseRedirect('/todo/')