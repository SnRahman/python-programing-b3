from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('product/add', views.add_product, name='add_product'),
    path('product/delete/<int:id>', views.delete_product,  name="delete_product"),
    path('product/edit/<int:id>', views.edit_product,  name="edit_product"),
    path('signup/', views.signup,  name="signup"),
    path('login/', views.user_login,  name="login"),
    path('logout/', views.user_logout,  name="logout"),
    path('profile/edit/', views.edit_profile,  name="edit_profile"),
    path('profile/change-password/', views.change_password,  name="change_password"),
]
