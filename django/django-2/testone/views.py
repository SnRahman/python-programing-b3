from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student

def home(request):
    return render(request,'homeone.html')


def display(request, id):
    return HttpResponse(f'name is {id}')

def lists(request):
    name = 'muzammil'
    courses = ['html' , 'css' , 'js' , 'python']

    return render(request,'list.html',{'name': name, 'courses': courses})

def dict(request):
    products = [
                {
                    'name' : 'TUC',
                    'details' : [
                        {
                            'qty' : 1000,
                            'size' : 'Half roll',
                            'price' : 40,

                        },
                        {
                            'qty' : 1000,
                            'size' : 'Tigi Pack',
                            'price' : 20,
                        },
                    ]
                },
                {
                    'name' : 'Sooper',
                    'details' : [
                        {
                            'qty' : 500,
                            'size' : 'Half roll',
                            'price' : 50,

                        },
                        {
                            'qty' : 1000,
                            'size' : 'Tigi Pack',
                            'price' : 25,
                        },
                    ]
                },
                {
                    'name' : 'Oreo',
                    'details' : [
                        {
                            'qty' : 5000,
                            'size' : 'Half roll',
                            'price' : 50,

                        },
                        {
                            'qty' : 2000,
                            'size' : 'Tigi Pack',
                            'price' : 25,
                        },
                    ]
                }
            ]
    
    return render(request,'dict.html',{'products':products})

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone = request.POST['phone']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            form_data = request.POST

            if first_name and last_name and email and phone and password and confirm_password and password == confirm_password:
                student =  Student(first_name = first_name, last_name= last_name, email=email,phone=phone,password = password)
                student.save()
                
                return redirect('students')
                # return render(request,'register.html',{'form_data': form_data})
            else:
                return HttpResponse('Invalid data')

def students_display(request):
    students = Student.objects.all()
    # return HttpResponse(students[0].id)
    return render(request,'students.html',{'students':students})

def student_delete(request,id):
    # student = Student.objects.get(id= id)
    student = Student.objects.get(pk= id)
    student.delete()
    return redirect('students')
    return HttpResponse(student)


    return HttpResponse(id)







def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        form_data = request.POST

        if first_name and last_name and email and phone and password and confirm_password and password == confirm_password:
            return render(request,'register.html',{'form_data': form_data})
        else:
            return HttpResponse('Invalid data')

    else:
        return HttpResponse('method not allowed.')
