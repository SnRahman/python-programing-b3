from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserCustomChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email')

    def __init__(self,*args, **kwargs):
        super(UserCustomChangeForm,self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'