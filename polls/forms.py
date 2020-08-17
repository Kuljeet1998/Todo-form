from django import forms
from .models import *
from django.shortcuts import render,get_object_or_404
class UserForm(forms.Form):
	id=forms.IntegerField()
	username=forms.CharField()
	first_name=forms.CharField()
	last_name=forms.CharField()

class CreatorForm(forms.Form):
	user=UserForm()
	new_notif=forms.IntegerField()

class AttachmentForm(forms.Form):
	document=forms.FileField()

	def clean(self):
		cleaned_data=super(AttachmentForm,self).clean()
		document=cleaned_data.get('document')
		if not document:
			raise forms.ValidationError("Cant be empty")

class TodoForm(forms.Form):
	title=forms.CharField()
	desc=forms.CharField()
	status=forms.IntegerField()
	creator=forms.ModelChoiceField(queryset=Creator.objects.all())
	attachment=forms.ModelMultipleChoiceField(queryset=Attachment.objects.all(),required=False)
	marked=forms.ModelMultipleChoiceField(queryset=Creator.objects.all(),required=False)


	def clean(self):
		cleaned_data=super(TodoForm,self).clean()
		title=cleaned_data.get("title")
		desc=cleaned_data.get("desc")
		status=cleaned_data.get("status")
		creator=cleaned_data.get("creator")
		attachment=cleaned_data.get("attachment")
		marked=cleaned_data.get("marked")

		if not title and not desc and not creator:
			raise forms.ValidationError("Cant be empty")
		print("submitted")
		todo=Todo(title=title,desc=desc,status=status,creator=creator)
		todo.save()
		todo.attachment.set(attachment)
		todo.marked.set(marked)

class NotificationForm(forms.Form):
	state=forms.IntegerField()
	new_state=forms.IntegerField()
	todo_user_id=forms.IntegerField()
	todos=forms.ModelChoiceField(queryset=Todo.objects.all())
	
class TodoPatchForm(forms.Form):
	status=forms.IntegerField()

	def clean(self):
		cleaned_data=super(TodoPatchForm,self).clean()
		status=cleaned_data.get("status")

		if not status:
			raise forms.ValidationError("Cant be empty")
		
	
	# def update(pk,instance):	
	# 	todo_object=get_object_or_404(Todo,id=pk)
	# 	if todo_object.status ==1 and status==2:
	# 		todo=Todo(title=todo_object.title,desc=todo_object.desc,status=status,creator=todo_object.creator)
	# 		todo.save()
	# 		todo.attachment.set(attachment)
	# 		todo.marked.set(marked)
	# 	elif todo_object.status==2 and status==3:
	# 		todo=Todo(title=todo_object.title,desc=todo_object.desc,status=status,creator=todo_object.creator)
	# 		todo.save()
	# 		todo.attachment.set(attachment)
	# 		todo.marked.set(marked)
	# 	elif todo_object.status==3:
	# 		todo=Todo(title=todo_object.title,desc=todo_object.desc,status=status,creator=todo_object.creator)
	# 		todo.save()
	# 		todo.attachment.set(attachment)
	# 		todo.marked.set(marked)
	# 	else:
	# 		HttpResponse("Not allowed !!")	