from django import forms
from ..models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    category = forms.CharField(max_length=200)
    brand = forms.CharField(max_length=200)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    weight = forms.DecimalField(max_digits=10, decimal_places=2)
    image = forms.ImageField()

    class Meta:
        model = Product
        fields = ('__all__')