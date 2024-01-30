from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import User
from .forms.user_create_form import UserForm
# Create your views here.


def signup(request):
    if request.method == 'GET':
        form = UserForm()
        # return HttpResponse(form)
        return render(request,'signup_form.html',{'form':form})
        # return render(request,'signup.html')
    else:
        form = UserForm( request.POST)
        if  form.is_valid():
            form.save()
            return redirect('users')
        else:
            return HttpResponse('invalid details entered!')

def signup0(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if first_name and last_name and email and phone and password and confirm_password and password==confirm_password:
            user = User(first_name=first_name,last_name=last_name,email=email,phone=phone,password=password)
            user.save()
            return redirect('users')
        else:
            return HttpResponse('invalid details entered!')


def display_users(request):
    users = User.objects.all()
    return render(request,'details.html',{'users':users})

def delete_user(request,id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('users')

def edit_user(request,id):
    user = User.objects.get(pk=id)

    if  request.method=='GET':
        # return HttpResponse(user)
        return render(request,'edit_user.html',{'user':user})
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']

        if first_name and last_name and email and phone:
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.phone = phone

            user.save()
            return HttpResponse('record updated')
        else:
            return HttpResponse('invalid details entered!')
        