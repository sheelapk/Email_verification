from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='first name.')
    last_name = forms.CharField(max_length=30, required=True, help_text='last name.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    # birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username','email', 'password1')