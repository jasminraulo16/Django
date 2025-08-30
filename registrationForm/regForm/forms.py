from django import forms
from .models import UserRegister
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserRegister
        fields=('door_no','street','landmark','city','state','zipcode','userpic')
    captcha = ReCaptchaField()