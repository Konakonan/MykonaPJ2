from django.db import models
from django.utils import timezone

class Company_name(models.Model):
    name=models.CharField("派遣会社名",max_length=30)
    created_at=models.DateTimeField("日付", default=timezone.now)
        
    def __str__(self) :
        return self.name
    
class Syukkin_yobi(models.Model):
    name=models.CharField("曜日",max_length=10 )
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    GENDER_CHOICES = (
        (1, "男"),
        (2, "女"),
        (3,"その他")
    )
    employee_id=models.IntegerField("社員ID", primary_key=True,blank=False,null=False)
    first_name=models.CharField("姓", max_length=20)
    last_name=models.CharField("名", max_length=20)
    gender = models.IntegerField("性別", choices=GENDER_CHOICES,null=True, blank=True)
    email=models.EmailField("メールアドレス", blank=True)
    company_name=models.ForeignKey(
        Company_name,verbose_name="派遣会社", on_delete=models.PROTECT,null=True, blank=True)
    syukkin_yobi=models.ManyToManyField(
        Syukkin_yobi,verbose_name="出勤曜日")
    created_at=models.DateTimeField("日付", default=timezone.now)
    
    def __str__(self):
        return "{0}  {1}{2}  {3} ".format(self.employee_id, self.first_name, self.last_name,self.company_name)