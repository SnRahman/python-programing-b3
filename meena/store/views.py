from django.shortcuts import render, redirect

# Create your views here.
def shop(request):
    return render(request,'shop.html')

def user_signup(request):
    return render(request,'signup.html')

def user_login(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def edit_profile(request):
    return render(request,'edit_profile.html')

def change_password(request):
    return render(request,'change_password.html')

def show_cart(request):
    return render(request,'show_cart.html')

def checkout(request):
    return render(request,'checkout.html')

def product(request,id):
    return render(request,'product.html')

def add_to_cart(request):
    return redirect('show_cart')