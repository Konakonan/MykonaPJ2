from django import forms 
from .models import Syukkin_yobi

class SerchForm(forms.Form):
    syukkin_yobi=forms.ModelChoiceField(
        queryset=Syukkin_yobi.objects, label="曜日", required=False
    )