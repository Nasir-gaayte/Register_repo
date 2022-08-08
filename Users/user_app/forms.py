from django import forms
from .models import UserRegisterModel



class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta():
        model = UserRegisterModel
        fields = '__all__'
        
        
