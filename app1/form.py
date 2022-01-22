from django import forms

from app1 import models
from app1.models import Account, Employee


class Acntmform(forms.ModelForm):
    class Meta:
        model=Account
        fields='__all__'
        #fields=['acc_no',acc_holder','atm','cvv']

        exclude=('status',)

class Addempform(forms.ModelForm):
    class Meta:
        model=Employee
        fields = '__all__'

class Udetails(forms.Form):
    fname1=forms.CharField(label="First Name",max_length=100)
    lname1=forms.CharField(label="Last Name",max_length=100)
    age1=forms.IntegerField(label="Age")

class EmployeeForm(forms.Form):
    emp_name1 = forms.CharField(label="Employee_Name",max_length=20)
    emp_email1 = forms.EmailField(label="Email",max_length=20)
    emp_ph1= forms.IntegerField(label="Phone")
    emp_dept1 = forms.CharField(label="Department",max_length=20)
    emp_username1=forms.CharField(label="Username",max_length=20)
    emp_password1=forms.CharField(label="Password",max_length=20)
    status1 = forms.CharField(label="Status",max_length=10)
