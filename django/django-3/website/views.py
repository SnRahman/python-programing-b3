from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms.product_form import ProductForm
from .models import Product
from django.contrib import messages

# Create your views here.

def dashboard(request):
    products = Product.objects.all()
    # return HttpResponse(products[0].price)
    return render(request,'dashboard.html',{'products':products})

def signup(request):
    if request.method == 'GET':
        form = ProductForm()
        # return HttpResponse(form)
        return render(request,'add_product.html',{'form':form})
    else:
        form = ProductForm( request.POST,request.FILES )
        if form.is_valid():
            form.save()
            messages.success(request,"Product has been added Successfully!")
            return redirect('dashboard')
        else:
            messages.error(request,"Error Occurred while adding product.")
            return redirect('signup')
        
def edit_product(request,id):
    product = Product.objects.get(pk=id)
    if request.method == 'GET':
        form =  ProductForm(instance=product)
        # return HttpResponse(id)
        return render(request,'edit_product.html',{'form':form, 'id':id })
    else:
        form = ProductForm(request.POST, request.FILES, instance=product )
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse(form.errors)

def delete_product(request,id):
    product=Product.objects.get(pk=id)
    product.delete()
    return redirect('dashboard')

