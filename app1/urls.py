from django.conf.urls.static import static
from django.urls import path

from app1 import views
from mainpro import settings

urlpatterns=[
    path('index/', views.indexpage),
    path('custmrbse/', views.customerbasepg),
    path('order/', views.orderpage),
    path('custreg/', views.customerregdb),
    path('custview/', views.adminviewcustomers),
    path('shopreg/', views.shopregdb),
    path('adfood/', views.addfood),

    path('viewmenu/', views.custviewmenu),
    path('viewonecust/', views.viewonecust),
    path('updateage/', views.updateage),
    path('updatemail/', views.updatemail),
    path('adviewmenu/', views.adviewmenu),
    path('adaccnt/', views.addaccount),
    path('accountdb/', views.accountdb),
    path('addemp/', views.addemployee),
    path('employeedb/', views.employeedb),
    path('addudata/', views.udata),
    path('login/', views.login),
    path('logout/', views.logout),
    path('mail/', views.mailsend),
    path('foodorder/', views.foodorder),
    path('vieworder/', views.vieworderdetails),
    path('viewemp/', views.viewemp),

    path('msgpage/', views.msgpage),
    path('sendmail/', views.sendmail),
    path('empreg/', views.empreg),
    path('update_email/', views.updatee),

    path('updatee/', views.update),
    path('new/', views.new),




]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)