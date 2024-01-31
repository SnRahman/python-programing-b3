from django import forms
from ..models import User


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150)
    # last_name = forms.CharField(max_length=150,required=False)
    email = forms.EmailField()
    phone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=20)
    confirm_password = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('first_name','last_name')
        # fields = ('__all__')


# class UserForm(forms.Form):
#     first_name = forms.CharField(max_length=150)
#     last_name = forms.CharField(max_length=150,required=False)
#     email = forms.EmailField()
#     phone = forms.CharField(max_length=11)
#     password = forms.CharField(max_length=20)
#     confirm_password = forms.CharField(max_length=20)