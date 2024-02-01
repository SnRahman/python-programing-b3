from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('product/delete/<int:id>', views.delete_product,  name="delete_product"),
    path('product/edit/<int:id>', views.edit_product,  name="edit_product"),
]
