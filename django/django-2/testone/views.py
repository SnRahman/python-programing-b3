from django.shortcuts import render
from django.http import HttpResponse
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