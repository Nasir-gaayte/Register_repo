from tkinter import Widget
from django import forms
from .models import UserRegisterModel


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = UserRegisterModel
        fields = '__all__'