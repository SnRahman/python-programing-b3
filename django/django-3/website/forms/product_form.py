from django import forms
from ..models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=200 , widget= forms.TextInput( attrs= {'class' : 'form-control '} ) )
    category = forms.CharField(max_length=200, widget= forms.TextInput( attrs= {'class': 'form-control py-1 category-input'} ) )
    brand = forms.CharField(max_length=200 , widget= forms.TextInput( attrs= {'class': 'form-control py-1 category-input'} ))
    price = forms.DecimalField(max_digits=10, decimal_places=2 , widget= forms.NumberInput( attrs= {'class': 'form-control py-1 category-input'} ))
    weight = forms.DecimalField(max_digits=10, decimal_places=2 , widget= forms.NumberInput( attrs= {'class': 'form-control py-1 category-input'} ))
    image = forms.ImageField(widget= forms.FileInput( attrs= {'class': 'form-control py-1 category-input'} ))

    class Meta:
        model = Product
        fields = ('__all__')