from django.urls import path
from.import views

urlpatterns = [
     path("home/",views.home),
     path('index/',views.index),

     # path('details/<id>/',views.details)
     path('details/<int:id>/',views.details),
     path('display/',views.display),
     path('display-dictionary/',views.display_dict)
]
