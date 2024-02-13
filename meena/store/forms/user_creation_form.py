from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCustomCreationForm(UserCreationForm):
    # first_name = forms.CharField(max_length=150)
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')

    def __init__(self, *args , **kwargs ):
        super(UserCustomCreationForm,self).__init__(*args , **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-inputs'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'

        self.fields['last_name'].widget.attrs['class'] = 'form-inputs'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'

        self.fields['username'].widget.attrs['class'] = 'form-inputs'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'

        self.fields['email'].widget.attrs['class'] = 'form-inputs'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

        self.fields['password1'].widget.attrs['class'] = 'form-inputs'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'

        self.fields['password2'].widget.attrs['class'] = 'form-inputs'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'



    





