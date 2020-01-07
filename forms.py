from django import forms
from appone.models import Logs

class new_form(forms.ModelForm):
    #re-enter_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Logs
        widgets = { 'password': forms.PasswordInput(),}
        labels = {"name": "Username" }
        fields ='__all__'
        
class login_form(forms.ModelForm):
    class Meta:
        model=Logs
        exclude=['email',]
