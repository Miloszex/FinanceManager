from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.forms import ModelForm



class LoginForm(forms.Form):
	username = forms.CharField(label='Username')
	password = forms.CharField(label='Password', widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')
