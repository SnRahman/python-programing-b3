from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms.product_form import ProductForm
from .models import Product
from django.contrib import messages
from django.contrib.auth.models import User

# user auth functions
from django.contrib.auth import authenticate , login , logout , update_session_auth_hash

# user built in forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm , PasswordChangeForm

# user custom forms
from .forms.user_creation_form import UserCustomCreationForm
from .forms.user_update_form import UserCustomChangeForm




# Create your views here.

def dashboard(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        # return HttpResponse(products[0].price)
        return render(request,'dashboard.html',{'products':products})
    else:
        messages.info(request,'Please login first!')
        return redirect('login')

def add_product(request):
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
            return redirect('add_product')
        
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


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            # form = UserCreationForm()
            form = UserCustomCreationForm()
            # return HttpResponse(form)
            return render(request,'signup.html',{'form':form})
        else:
            # form_data = UserCreationForm( request.POST )
            form_data = UserCustomCreationForm( request.POST )
            if form_data.is_valid():
                form_data.save()
                messages.success(request,'User Registered Successfully!')
                return redirect('dashboard')
            else:
                messages.error(request,'Please provide correct information.')
                return redirect('signup')
    else:
        return redirect('dashboard')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            return render(request,'login.html')
            # return HttpResponse(request.user.is_authenticated) 
        else:
            # return HttpResponse(request.POST)
            username = request.POST['email']
            password = request.POST['password']

            if username and password:
                # built in function to authenticate user record
                user = authenticate(request,username=username,password=password)
                if user is None:
                    messages.error(request,'No user Found.')
                    return redirect('login')
                else:
                    login(request,user)
                    messages.success(request,'Login successfully!')
                    return redirect('dashboard')
            else:
                messages.error(request,'Invalid credentials')
                return redirect('login')
    else:
        return redirect('dashboard')

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("login")

def edit_profile(request):
    if  request.method=='GET':
        form = UserCustomChangeForm(instance = request.user )
        # return HttpResponse(form)
        return render(request,'edit_profile.html', {'form':form} )
    else:
        form = UserCustomChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile updated Successfully.")
            return redirect('dashboard')
        else:
            messages.warning(request, 'Please correct the error below.')
            return redirect('edit_profile')
        
def change_password(request):
    # return HttpResponse(form)
    if  request.method=='GET':
        form = PasswordChangeForm(request.user)
        # return HttpResponse(form)
        return render(request,'change_password.html', {'form':form} )
    else:
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"Password updated Successfully.")
            return redirect('dashboard')
        else:
            messages.warning(request, 'Please correct the error below.')
            return redirect('change_password')