from django.urls import path
from . import views
urlpatterns = [
    path('signin/',views.signup,name='signin'),
    path('users/',views.display_users,name='users'),
    path('delete/<int:id>',views.delete_user,name='delete'),
    path('edit/<int:id>',views.edit_user,name='edit_user')
]
