from django.db import models

# Create your models here.
class Customer(models.Model):
    fname=models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    age = models.IntegerField()
    email= models.EmailField(max_length=20)
    Uname = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    pics = models.CharField(max_length=200,default='null')
    document = models.CharField(max_length=200,default='null')


class Shopping(models.Model):
    fname=models.CharField(max_length=20)
    lname = models.CharField (max_length=20)
    phone = models.IntegerField()
    email= models.EmailField(max_length=20)
    item=models.CharField(max_length=20)
    quantity=models.IntegerField()
    Uname = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

class Menu(models.Model):
    name=models.CharField(max_length=50)
    category =models.CharField(max_length=20)
    price =models.IntegerField()

class Account(models.Model):
    acc_no=models.CharField(max_length=12,unique=True)
    acc_holder=models.CharField(max_length=20)
    atm=models.CharField(max_length=12)
    cvv=models.CharField(max_length=4)
    status=models.CharField(max_length=10,default='Active')

class Employee(models.Model):
    emp_name= models.CharField(max_length=20)
    emp_email = models.CharField(max_length=20,unique=True)
    emp_ph= models.IntegerField()
    emp_dept = models.CharField(max_length=20)
    emp_username=models.CharField(max_length=20)
    emp_password=models.CharField(max_length=20)
    status = models.CharField(max_length=10, default='Active')



class Userdetails(models.Model):
    fname= models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    age= models.IntegerField()



class Admin(models.Model):
    uname=models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Orders(models.Model):
    oid=models.AutoField(primary_key=True)
    cid=models.ForeignKey(Customer,on_delete=models.CASCADE)
    fname=models.CharField(max_length=100)
    quantity=models.IntegerField()
    price=models.FloatField()

