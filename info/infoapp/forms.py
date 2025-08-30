from django import forms
from infoapp.models import userDetails

class UserForm(forms.ModelForm):
    class Meta:
        model = userDetails
        fields = "__all__"