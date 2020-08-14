from django.shortcuts import render
from .forms import *
# Create your views here.

def home(request):
	if request.method=='POST':
		form=CreatorForm(request.POST)
		if form.is_valid():
			pass
	else:
		form=CreatorForm()
	return render(request,'home.html',{'form':form})

def fileupload(request):
	if request.method=='POST':
		form=AttachmentForm(request.POST)
		if form.is_valid():
			pass
	else:
		form=AttachmentForm()

	return render(request,'fileupload.html',{'form':form})

def todo(request):
	
	if request.method=='POST':
		form=TodoForm(request.POST)
		if form.is_valid():
			pass
	else:
		form=TodoForm()
		todo_list=Todo.objects.all()
	return render(request,'todo.html',{'form':form,'todo_list':Todo.objects.all()})

