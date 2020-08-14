from django import forms
from .models import *
from django.shortcuts import render
class UserForm(forms.Form):
	id=forms.IntegerField()
	username=forms.CharField()
	first_name=forms.CharField()
	last_name=forms.CharField()

class CreatorForm(forms.Form):
	user=UserForm()
	new_notif=forms.IntegerField()

class AttachmentForm(forms.Form):
	# id=forms.IntegerField()
	document=forms.FileField()

	def clean(self):
		cleaned_data=super(AttachmentForm,self).clean()
		# id=cleaned_data.get('id')
		document=cleaned_data.get('document')
		if not document:
			raise forms.ValidationError("Cant be empty")

class TodoForm(forms.Form):
	# id=forms.IntegerField()
	title=forms.CharField()
	desc=forms.CharField()
	status=forms.IntegerField()
	# created=forms.DateTimeField()
	# updated=forms.DateTimeField()
	creator=forms.ModelChoiceField(queryset=Creator.objects.all())
	# attachment=forms.ModelMultipleChoiceField(queryset=Attachment.objects.all(),required=False)
	# attachment_details=AttachmentForm(read_only=True,many=True,source='attachment')
	# marked=forms.ModelMultipleChoiceField(queryset=Creator.objects.all(),required=False)
	# marked_details=UserForm(read_only=True,many=True)


	def clean(self):
		cleaned_data=super(TodoForm,self).clean()
		# id=cleaned_data.get("id")
		title=cleaned_data.get("title")
		desc=cleaned_data.get("desc")
		status=cleaned_data.get("status")
		# created=cleaned_data.get("created")
		# updated=cleaned_data.get("updated")
		creator=cleaned_data.get("creator")
		# attachment=cleaned_data.get("attachment")
		# marked=cleaned_data.get("marked")

		if not title and not desc and not creator:
			raise forms.ValidationError("Cant be empty")
		print("submitted")
		todo=Todo(title=title,desc=desc,status=status,creator=creator)
		todo.save()

		

# class NotificationForm(forms.Form):
# 	id=forms.IntegerField(read_only=True)
# 	state=forms.IntegerField()
# 	new_state=forms.IntegerField()
# 	todo_user_id=forms.IntegerField()
# 	todos=forms.ModelChoiceField(queryset=Todo.objects.all())
	
