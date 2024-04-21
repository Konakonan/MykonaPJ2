from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Employee
from .forms import SerchForm
from django.shortcuts import redirect
from django.db.models.query import QuerySet


def post_list(request):
    posts = Employee.objects.all()
    # return　返す、 render 表示、 gyoumu~t.html　このページ、 {'posts':post}　postsにpostsを代入
    return render(request, 'gyoumuhyo/post_list.html', {'posts':posts})

def post_list2(request):
    form=SerchForm()
    if request.method=="GET":
        form=SerchForm(request.GET)
        form.is_valid()
        
        queryset=Employee.objects.all()
        
        syukkin_yobi=form.cleaned_data['syukkin_yobi']
        if syukkin_yobi:
            queryset=queryset.filter(syukkin_yobi=syukkin_yobi)
            #　ランダムに[:数字]個　表示させる処理
            queryset = queryset.order_by('?')[:1]
            posts=queryset
            return render(request, 'gyoumuhyo/post_list2.html', {'posts':posts})
            
    else:
        form=SerchForm()
        
    return render(request, 'gyoumuhyo/post_list2.html', {'form':form}) 