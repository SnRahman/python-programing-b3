from django.contrib import admin
from .models import Product, Category, Cart, Order
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','price','description','is_sale','sale_price')

class  CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class CartAdmin(admin.ModelAdmin):
    list_display = ('id','product','user','quantity','sub_total','order_id')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','address','city','phone','email')

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(Order,OrderAdmin)
