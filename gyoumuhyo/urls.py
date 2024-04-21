from django.urls import path
from . import views

app_name="gyoumuhyo"

urlpatterns=[
   path("", views.post_list, name='post_list'),
   path("post/list2/", views.post_list2, name='post_list2')
]