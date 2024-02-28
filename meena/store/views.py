from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , UserChangeForm , PasswordChangeForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms.user_creation_form import UserCustomCreationForm
from .forms.user_change_form import UserCustomChangeForm
from .forms.password_change_form import PasswordCustomChangeForm
from .forms.checkout_form import Checkout
from .models import Product, Category, Cart
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader

# Create your views here.
def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    # return HttpResponse(products)
    return render(request,'shop.html', {'products':products , 'categories' : categories})

def category_filter(request,id):
    categories = Category.objects.all()
    category = Category.objects.get(pk = id)
    products = Product.objects.filter(category= category)
    if products is None or len(products) == 0:
        messages.info(request,"No product in this category")
        return redirect('shop')
        
    return render(request,'shop.html', {'products':products , 'categories' : categories})

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



def send_email():
    subject = 'testing'
    message = "This is a sample email"
    form = settings.EMAIL_HOST_USER
    to = ['pehlidachan@gmail.com']
    send_mail(subject,message,form,to)

def send_email_template(cart_items,shipping_charges,sub_total,grand_total,email):
    subject = 'testing'
    form = settings.EMAIL_HOST_USER
    to = email

    # text_file = loader.render_to_string('email_template.txt')
    # html_file = loader.render_to_string('email_template.html')

    text_file = loader.render_to_string('order_email.txt',{'cart_items': cart_items,'shipping_charges':shipping_charges, 'sub_total':sub_total, 'grand_total' : grand_total})
    html_file = loader.render_to_string('order_email.html',{'cart_items': cart_items,'shipping_charges':shipping_charges, 'sub_total':sub_total, 'grand_total' : grand_total})


    send_mail(subject,text_file,form,to, html_message=html_file)


def about(request):
    # send_email_template()
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
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user, order_id=0)
        sub_total = 0.00
        shipping_charges = 5.00
        for  item in cart_items:
            # sub_total += float(item.product.price) * item.quantity
            sub_total += float(item.sub_total)

        grand_total = sub_total + shipping_charges
        # return HttpResponse(grand_total)
        return render(request,'show_cart.html' , {'cart_items': cart_items, 'shipping_charges':shipping_charges, 'sub_total':sub_total, 'grand_total' : grand_total})
    else:
        messages.warning(request,'Kindly login first.')
        return redirect('login')
def checkout(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user,order_id=0)
        sub_total = 0.00
        shipping_charges = 5.00
        for  item in cart_items:
            # sub_total += float(item.product.price) * item.quantity
            sub_total += float(item.sub_total)

        grand_total = sub_total + shipping_charges

        if request.method =='GET':
            checkout_form = Checkout()
            return render(request,'checkout.html', { "form" : checkout_form ,'cart_items': cart_items, 'shipping_charges':shipping_charges, 'sub_total':sub_total, 'grand_total' : grand_total})
        else:
            checkout_form = Checkout(request.POST)
            if checkout_form.is_valid():
                order = checkout_form.save()
                for item in cart_items:
                    item.order_id = order.id
                    item.save()

                send_email_template(cart_items,shipping_charges,sub_total,grand_total,checkout_form['email'])
                messages.success(request,"Your order has been placed")
                return redirect('shop')
            else:
                for error in checkout_form.errors:
                    messages.error(request,f'provide valid information in {error}')
                return redirect('checkout') 
    else:
        messages.warning(request,'Kindly login first.')
        return redirect('login')


def product(request,id):
    product = Product.objects.get(pk=id)
    return render(request,'product.html',{'product': product})

def add_to_cart(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            product_id = request.POST['product_id']
            qty = request.POST['qty']
            product = Product.objects.get(pk=product_id)
            sub_total = int(qty) * product.price
            
            try:
                cart = Cart.objects.get(product = product, user= request.user, order_id = 0)
            except:
                cart = None

            if cart is None:
                # user = request.user
                cart = Cart(product = product, user = request.user, quantity=qty, sub_total = sub_total )
                cart.save()
            else:
                cart.quantity += int(qty)
                cart.sub_total += sub_total
                cart.save()

            messages.success(request,'Product added in cart Successfully!')
            # return HttpResponse(request.POST)
        
            return redirect('show_cart')
        else:
            messages.warning(request,'Method not allowed.')
            return redirect('shop')
    else:
        messages.warning(request,'Kindly login first.')
        return redirect('login')
