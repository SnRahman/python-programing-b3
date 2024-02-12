from django.urls import path
from . import views

urlpatterns = [
    path('',views.shop , name='shop'),
    path('signup/',views.user_signup , name='signup'),
    path('login/',views.user_login , name='login'),
    path('about/',views.about , name='about'),
    path('contact/',views.contact , name='contact'),
    path('profile/edit/',views.edit_profile , name='edit_profile'),
    path('profile/change-password/',views.change_password , name='change_password'),
    path('cart/show/',views.show_cart , name='show_cart'),
    path('checkout/',views.checkout , name='checkout'),
    path('product/<int:id>',views.product , name='product'),
    path('cart/add/',views.add_to_cart , name='add_to_cart'),
]
