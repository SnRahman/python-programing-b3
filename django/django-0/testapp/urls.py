from django.urls import path
# from .views import home , index
from . import views


urlpatterns = [
    path('',views.home),
    path('index/',views.index),
    path('shop/',views.shop)
    # path('home/',home)
]
