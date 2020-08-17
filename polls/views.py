from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
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
		# todo_list=Todo.objects.all()
	return render(request,'todo.html',{'form':form,'todo_list':Todo.objects.all()})

def todo_detail(request,pk):
	return render(request,'todo_detail.html',{'todo_detail':get_object_or_404(Todo,id=pk)})

def todo_delete(request,pk):
	todo_object=get_object_or_404(Todo,id=pk)
	todo_object.delete()
	return HttpResponse('Todo deleted successfully !!')

def todo_patch(request,pk=None):
	
	if request.method=='POST':
		print("adasadasdadad")
		form=TodoPatchForm(request.POST)
		# import pdb;
		# pdb.set_trace()

		if form.is_valid():
			todo_object=get_object_or_404(Todo,id=pk)
			state=form.cleaned_data.get('status',None)
			if todo_object.status ==1 and state==2:
				todo_object.status=state
				todo_object.save()
			elif todo_object.status==2 and state==3:
				todo_object.status=state
				todo_object.save()
			elif todo_object.status==3:
				todo_object.status=state
				todo_object.save()
			else:
				HttpResponse("Not allowed !!")	
		return render(request,'todo_detail.html',{'todo_detail':todo_object})
	else:
		form=TodoPatchForm()
		return render(request,'todo_patch.html',{'form':form,'todo_list':Todo.objects.all()})