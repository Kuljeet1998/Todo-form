from django.urls import path
from .views import *
from polls import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from .views import *
urlpatterns=[
	path('creator/',views.home),
	path('fileupload/',views.fileupload),
	path('todo/',views.todo),
	path('todo/<int:pk>/',views.todo_detail),
	path('todo/<int:pk>/delete/',views.todo_delete),
	path('todo/patch/',views.todo_patch,name="patch"),
]