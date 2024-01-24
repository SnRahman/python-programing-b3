from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("hello class!")
    return HttpResponse("<h1> hello class! </h1>")

def index(request):
    return render(request,'home.html')


def details(request,id):
    return HttpResponse(f'detials id is : {id}')

def display(request):
    name = 'Ahmad'
    age = 25

    courses = ['web Development','Python Programing','App development','Game development','Digital Marketing','Customer support']
    courses1 = courses[:3]
    courses2 = courses[3:]
     
    # return HttpResponse(courses[0])


    return render(request,'display.html',{'name':name,'age':age,'courses1':courses1 ,'courses2':courses2})

def display_dict(request):
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
    
    # return HttpResponse(products[2]['details'])


    return render(request,'dict.html',{'products':products})