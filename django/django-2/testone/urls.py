from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('display/<int:id>/',views.display),
    path('lists/',views.lists),
    path('dict/',views.dict),
    path('signup/',views.signup),
    path('register/',views.register,name='register')
]
