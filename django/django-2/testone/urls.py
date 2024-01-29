from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('display/<int:id>/',views.display),
    path('lists/',views.lists),
    path('dict/',views.dict),
    path('signup/',views.signup , name='signup'),
    path('register/',views.register,name='register'),
    path('students/',views.students_display, name="students"),
    path('student/delete/<int:id>',views.student_delete, name="delete_student"),
]
