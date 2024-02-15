from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , UserChangeForm , PasswordChangeForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms.user_creation_form import UserCustomCreationForm
from .forms.user_change_form import UserCustomChangeForm
from .forms.password_change_form import PasswordCustomChangeForm
from .models import Product, Category


# Create your views here.
def shop(request):
    products = Product.objects.all()
    # return HttpResponse(products)
    return render(request,'shop.html', {'products':products})

def user_signup(request):
    form = UserCustomCreationForm()
    # return HttpResponse(form)
    return render(request,'signup.html',{'form':form})

def user_register(request):
    if  request.method == 'POST':
        form = UserCustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registered Successfully!.')
            return redirect('shop')
        else:
            for error in form.errors:
                messages.error(request,f'provide valid information in {error}')

            # messages.error(request,'Provide valid information.')
            return redirect('signup')
        # return HttpResponse(request)
    else:
        messages.info(request,'Method not allowed.')
        return redirect('login')

def user_login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username=request.POST['username']
        password = request.POST['password']

        if username and password:
            user = authenticate(request,username=username, password=password)

            if user is None:
                messages.error(request,'User does not exist!')
                return redirect('login')
            else:
                messages.success(request,'You are successfully logged in.')
                login(request,user)
                return redirect('shop')
        else:
            messages.error(request,'Provide valid information.')
            return redirect('login')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logged out Successfully!')
    return redirect('shop')



def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = UserCustomChangeForm(instance = request.user)
            # return HttpResponse(form)
            return render(request,'edit_profile.html' ,{'form':form} )
        else:
            form = UserCustomChangeForm(request.POST,instance = request.user)
            if form.is_valid():
                form.save()
                messages.success(request,"Profile Updated Successfully")
            else:
                for error in form.errors:
                    messages.error(request,f'provide valid information in {error}')

            return redirect('edit_profile')
    else:
        return redirect('shop')

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = PasswordCustomChangeForm(request.user)
            # return HttpResponse(form)
            return render(request,'change_password.html', {'form' : form})
        else:
            form = PasswordCustomChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request,user)
                messages.success(request,'password updated successfully!')
                return redirect('shop')
            else:
                for error in form.errors:
                    messages.error(request,f'provide valid information in {error}')
                return redirect('change_password') 
    else:
        return redirect('shop')

def show_cart(request):
    return render(request,'show_cart.html')

def checkout(request):
    return render(request,'checkout.html')

def product(request,id):
    product = Product.objects.get(pk=id)
    return render(request,'product.html',{'product': product})

def add_to_cart(request):
    return redirect('show_cart')