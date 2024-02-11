from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

class UserCustomCreationForm(UserCreationForm):
    # first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()



    class Meta:
        fields = ('username', 'first_name','last_name', 'email','password1','password2')
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'

        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'





