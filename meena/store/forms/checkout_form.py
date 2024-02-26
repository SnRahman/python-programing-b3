from django import forms
from ..models import Order
class Checkout(forms.ModelForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150,required=False)
    address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()

    class Meta:
        model = Order
        # fields = ('old_password','new_password1','new_password2')
        fields = ('__all__')


    def __init__(self,*args,**kwargs):
        super(Checkout,self).__init__(*args,**kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control nav-search'
        self.fields['last_name'].widget.attrs['class'] = 'form-control nav-search'
        self.fields['address'].widget.attrs['class'] = 'form-control nav-search'
        self.fields['city'].widget.attrs['class'] = 'form-control nav-search'
        self.fields['phone'].widget.attrs['class'] = 'form-control nav-search'
        self.fields['email'].widget.attrs['class'] = 'form-control nav-search'