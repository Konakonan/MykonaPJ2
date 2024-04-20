from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone
from . models import Employee

def post_list(request):
    posts = Employee.objects.all()
    return render(request, 'gyoumuhyo/post_list.html', {'posts':posts})
