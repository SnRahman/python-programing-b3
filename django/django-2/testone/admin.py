from django.contrib import admin
from .models import  Student, Employee


class StudentAdmin(admin.ModelAdmin):
    list_display =  ('id','first_name','last_name','email','phone')

class  EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','f_name','l_name','email','phone')


# Register your models here.
admin.site.register(Student,StudentAdmin)
admin.site.register(Employee,EmployeeAdmin)
