from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms.product_form import ProductForm


# Create your views here.

def dashboard(request):
    return HttpResponse('hello!')

def signup(request):
    if request.method == 'GET':
        form = ProductForm()
        # return HttpResponse(form)
        return render(request,'signup.html',{'form':form})
    else:
        form = ProductForm( request.POST,request.FILES )
        if form.is_valid():
            form.save()
            return HttpResponse('form submitted')
        else:
            return redirect('signup')
