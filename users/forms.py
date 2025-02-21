

from django import forms

class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class AddForm(forms.Form):

    likes = forms.IntegerField()
    shares = forms.IntegerField()
    