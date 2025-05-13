from django import forms
from .models import user
class stuform(forms.ModelForm):
    class Meta:
        model=user
        fields=['name','email','password']
        
        
class teaform(forms.ModelForm):
    class Meta:
        model=user
        fields=['teacher','email','password']       
        