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


def todo_update(request,pk):
	todo_object=get_object_or_404(Todo,id=pk)
	if request.method=="POST":
		# import pdb;
		# pdb.set_trace()

		form=TodoPatchForm(data=request.POST)
		if form.is_valid():
			
			
			state=form.cleaned_data.get('status')
			
			if ((todo_object.status ==1 and state==3) or (todo_object.status ==2 and state==1)):
				HttpResponse("NOT ALLOWED !!!")
			else:
				todo_object.status=state
				
			title=form.cleaned_data.get("title")
			desc=form.cleaned_data.get("desc")
			creator=form.cleaned_data.get("creator")
			attachment=form.cleaned_data.get("attachment")
			marked=form.cleaned_data.get("marked")

			todo_object.title=title
			todo_object.desc=desc
			todo_object.creator=creator
			todo_object.save()

			return render(request,'todo.html',{'form':form,'todo_list':Todo.objects.all()})
	else:
		form=TodoPatchForm({'title':todo_object.title,'desc':todo_object.desc,'status':todo_object.status,'creator':todo_object.creator})
	return render(request,'todo.html',{'form':form,'todo_list':Todo.objects.all()})