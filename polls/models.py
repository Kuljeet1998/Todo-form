from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.
class Creator(models.Model):
	user=models.OneToOneField(User ,related_name="creator", on_delete=models.CASCADE)
	new_notif=models.IntegerField(default=0)

	def __str__(self):
		return self.user.first_name+" w "+str(self.new_notif)+" notification(s)"


class Attachment(models.Model):
	document=models.FileField(upload_to='document/')
	def __str__(self):
		return str(self.id)


class Todo(models.Model):
	state=((1,'To be done'),(2,'In progress'),(3,'Done'))
	title=models.CharField(max_length=25)
	desc=models.TextField(max_length=100)
	status=models.IntegerField(default=1,choices=state)
	created=models.DateTimeField(auto_now=True)
	updated=models.DateTimeField(auto_now=True)
	creator=models.ForeignKey(Creator,on_delete=models.CASCADE, related_name='creator')
	attachment=models.ManyToManyField(Attachment) #DELAY
	marked=models.ManyToManyField(Creator)
	
	def __str__(self):
		return self.title

class Notification(models.Model):
	state=models.IntegerField()
	new_state=models.IntegerField(default=0)
	todo_user_id=models.IntegerField(default=0)
	todos=models.ForeignKey(Todo,on_delete=models.CASCADE,related_name="todo")

	def __str__(self):
		str1="State "+str(self.state)+" changed to "+str(self.new_state)+" in "+str(self.todo_user_id)
		return str1