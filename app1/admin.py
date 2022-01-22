from django.contrib import admin

# Register your models here.
from app1 import models
from app1.models import Customer, Shopping, Account


class Customeradmin(admin.ModelAdmin):
    list_display=('fname','age','email')
admin.site.register(Customer,Customeradmin)


#class Shoppingadmin(admin.ModelAdmin):
admin.site.register(Shopping)
admin.site.register(Account)
