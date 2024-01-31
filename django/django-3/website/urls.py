from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashborad'),
    path('signup/', views.signup, name='signup')
]
