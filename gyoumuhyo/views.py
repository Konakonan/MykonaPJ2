from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Employee, SworkArea
from .forms import SerchForm
from django.shortcuts import redirect
from django.db.models.query import QuerySet

def sworkeria2(n):
    #list1の数字を変えることでエリアに振り分ける人数を変更できる
    list1=[3,3,2,2,2,2,5,1]
    list2=[]
    for i in range(8):
        for j in range(list1[i]):
            list2.append(n)
        n+=1
    return list2
list3=sworkeria2(1)

def post_list(request):
    posts = Employee.objects.all()
    # return　返す、 render 表示、 gyoumu~t.html　このページ、 {'posts':post}　postsにpostsを代入
    return render(request, 'gyoumuhyo/post_list.html', {'posts':posts})

def post_list2(request):
    form=SerchForm()
    saria=[]
    for i in list3:
        saria.append(SworkArea.objects.get(pk=i))
    if request.method=="GET":
        form=SerchForm(request.GET)
        form.is_valid()
        
        queryset=Employee.objects.all()
        
        syukkin_yobi=form.cleaned_data['syukkin_yobi']
        if syukkin_yobi:
            queryset=queryset.filter(syukkin_yobi=syukkin_yobi)
            #　ランダムに[:数字]個　表示させる処理
            queryset = queryset.order_by('?')[:20]
            posts=queryset
            return render(request, 'gyoumuhyo/post_list2.html', {'posts':posts, 'saria':saria})
            
    else:
        form=SerchForm()
        
    return render(request, 'gyoumuhyo/post_list3.html', {'form':form}) 

        