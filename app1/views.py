from django.contrib.sessions.models import Session
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app1.form import Acntmform, Addempform, Udetails, EmployeeForm
from app1.models import Customer, Shopping, Menu, Userdetails, Admin, Employee, Orders
from mainpro.settings import EMAIL_HOST_USER


def indexpage(request):
    return render(request,'index.html')
def customerbasepg(request):
    return render(request,'customer/customerbase.html')
def orderpage(request):
    return render(request,'customer/order.html')
def customerregdb(request):
    if request.method=="POST" and request.FILES['doc'] and request.FILES['pic']:
        uploaded_file1=request.FILES['doc']
        fs=FileSystemStorage()
        fname1=uploaded_file1.name
        fdata1=fs.save(fname1,uploaded_file1)
        uploaded_file_url1=fs.url(fdata1)

        uploaded_file2 = request.FILES['pic']
        fs = FileSystemStorage()
        fname2 = uploaded_file2.name
        fdata2 = fs.save(fname2,uploaded_file2)
        uploaded_file_url2 = fs.url(fdata2)

        cust=Customer(fname=request.POST.get("fname"),
                      lname=request.POST.get("lname"),
                      age=request.POST.get("age"),
                      email=request.POST.get("mail"),
                      Uname=request.POST.get("uname"),
                      password=request.POST.get("psswrd"),
                      pics=uploaded_file_url2,
                      document=uploaded_file_url1)
        cust.save()

        return render(request, 'index.html')

def adminviewcustomers(request):
    cust1=Customer.objects.all()
    return render(request,'admin/viewcustomers.html',{"cdata":cust1})

def shopregdb(request):
    if request.method=="POST":
        shoporder=Shopping(fname=request.POST.get("fname"), lname=request.POST.get("lname"),
                      phone=request.POST.get("phone"),email=request.POST.get("mail"),item=request.POST.get("item"),
                      quantity=request.POST.get("quantity"),Uname=request.POST.get("uname"),
                      password=request.POST.get("password"))
        shoporder.save()

        return render(request, 'index.html')

def addfood(request):
    if request.method=="POST":
        obj=Menu(name=request.POST.get("fname"),category=request.POST.get("cat"),
                      price=request.POST.get("price"))
        obj.save()
        #obj=Menu.objects.all()
        #return render(request, 'admin/addfood.html',{'data':obj})
    return render(request,'admin/addfood.html')

def custviewmenu(request):
    if request.method=="POST":
        obj=Menu.objects.filter(category=request.POST.get('cat'))
        return render(request,'customer/viewmenu.html',{"food":obj})
    obj=Menu.objects.all()
    return render(request, 'customer/viewmenu.html', {"food": obj})

def viewonecust(request):
    obj1 = Customer.objects.all()
    """if request.method=="POST":

        obj=Customer.objects.get(id=request.POST.get('uid'))
        return render(request,'admin/viewcustomers.html',{"data":obj,"data1":obj1})"""
    return render(request,'admin/viewcustomers.html',{"data1":obj1})

def updateage(request):
    if request.method=="POST":
        cus=Customer.objects.get(id=request.POST.get('cid'))
        cus.age=request.POST.get("agen")
        cus.save()
        obj1 = Customer.objects.all()
        return render(request,"admin/viewcustomers.html",{'data1':obj1,'msg':1})


def updatemail(request):
    if request.method == "POST":
        cust = Customer.objects.get(id=request.POST.get('cid'))
        cust.email = request.POST.get("emid")
        cust.save()
        obj1 = Customer.objects.all()
        return render(request, "admin/viewcustomers.html", {'data1': obj1, 'msg': 1})

def adviewmenu(request):

        obj1=Menu.objects.all()
        if request.method == "POST":
            Menu.objects.get(id=request.POST.get('fid')).delete()
            return render(request,'admin/viewmenu.html',{'items':obj1,'msg':1})

        return render(request, 'admin/viewmenu.html', {'items': obj1})





def addaccount(request):
    obj=Acntmform()
    return render(request,'customer/addaccount.html',{'formdata':obj})

def accountdb(request):
    if request.method == "POST":
        obj1=Acntmform(request.POST)
        if obj1.is_valid():
            obj1.save()
    return addaccount(request)

def addemployee(request):
    obj=Addempform()
    return render(request,'customer/addemployee.html',{'formdata':obj})

def employeedb(request):
    if request.method == "POST":
        obj1=Addempform(request.POST)
        if obj1.is_valid():
            obj1.save()
    return addemployee(request)






def udata(request):
    if request.method=='POST':
        obj=Userdetails(fname=request.POST.get("fname1"),lname=request.POST.get("lname1"),age=request.POST.get("age1"))
        obj.save()
        return render(request,'index.html')
    dform=Udetails()
    return render(request,'admin/adduser.html',{'f1':dform})




def login(request):
    utype=request.POST.get('utype')

    uname1=request.POST.get('uname')
    pwd=request.POST.get('pwd')
    #print('utype:{} uname:{} paswd:{}'.format(utype,uname1,pwd))
    if utype=='Admin':

        try:
            if Admin.objects.get(uname=uname1) is not None:
                #print("1")

                ad=Admin.objects.get(uname=uname1)
                if pwd==ad.password:
                    #print("2")
                    request.session['sid']=ad.uname
                    #return render(request,'admin/adduser.html')
                    request.method="GET"
                    return udata(request)
                else:
                    #print("3")
                    return HttpResponse("Incorrect Password")
        except:
            return HttpResponse("username doesn't exist")

    if utype=='Customer':

        try:
            if Customer.objects.get(Uname=uname1) is not None:

                cobj=Customer.objects.get(Uname=uname1)
                if pwd==cobj.password:
                    request.session['sid']=cobj.Uname
                    #request.method = "GET"
                    return render(request,'customer/viewemp.html')
                else:
                    return render(request,'index.html',{'msg':"Incorrect Password"})
        except:
            return render(request,'index.html', {'msg': "Incorrect Username"})



    if utype=='Employee':

        try:

            if Employee.objects.get(emp_username=uname1) is not None:


                eobj=Employee.objects.get(emp_username=uname1)

                if pwd==eobj.emp_password:

                    request.session['sid']=eobj.emp_username

                    return render(request,'index.html')
                else:
                    return HttpResponse("Incorrect Password")
        except:
            return HttpResponse("username doesn't exist")
    return render(request,'index.html')

def logout(request):
    print('1')
    Session.objects.all().delete()
    return render(request,'index.html')

        #return render(request,'index.html')

def mailsend(request):
    if request.method=='POST':
        subject=request.POST.get('subj')
        message=request.POST.get('msg')
        print(message)
        recepient=str(request.POST.get('mailid'))
        print(recepient)
        send_mail(subject,message,EMAIL_HOST_USER,[recepient],fail_silently=False)
        print('1')
        return render(request,'customer/viewemp.html')
    return render(request, 'customer/mail.html')

def foodorder(request):
    if request.method=='POST':
        foodname=request.POST.get('fname')
        price=request.POST.get('price')
        qunty=request.POST.get('qnt')
        total=int(price)*int(qunty)
        user=Customer.objects.get(Uname=request.session['sid'])
        obj=Orders(fname=foodname,quantity=qunty,price=total,cid=user)
        obj.save()
        return render(request,'customer/viewmenu.html')

def vieworderdetails(request):
    user=Customer.objects.get(Uname=request.session['sid'])
    foodobj=Orders.objects.filter(cid=user)
    return render(request,'Customer/order.html',{'orders':foodobj})


def viewemp(request):
    if request.method=="POST":
        obj=Employee.objects.filter(emp_dept=request.POST.get('dept'))
        deptmnt=request.POST.get('dept')
        print(deptmnt)
        return render(request,'customer/viewemp.html',{"data1":obj})
    obj=Employee.objects.all()
    return render(request,'customer/viewemp.html',{'data1':obj})

def msgpage(request):
    #cusemail=request.POST.get('fromemail')
    subject=request.POST.get('subj')
    message=request.POST.get('msg')
    print(subject,message)
    #print(deptmnt)
    return render(request,'customer/sendmail.html')

def sendmail(request):
    sub=request.POST.get('subj')
    msg=request.POST.get('msg')
    print(sub,msg)
    return render(request,'customer/sendmail.html')


def empreg(request):
    if request.method=="POST":
        obj=Employee(emp_name=request.POST.get("emp_name1"),emp_email=request.POST.get("emp_email1"),
                      emp_ph=request.POST.get("emp_ph1"),emp_dept=request.POST.get("emp_dept1"),emp_username=request.POST.get("emp_username1"),
                      emp_password=request.POST.get("emp_password1"),status=request.POST.get("status1"))
        obj.save()
        return render(request, 'index.html')
    eform = EmployeeForm()
    return render(request, 'admin/employeereg.html', {'f1':eform})

def update(request):
    if request.method=='POST':
        obj=Customer.objects.get(id=request.POST.get('cid'))
        obj.email=request.POST.get('emid')
        obj.save()
        obj1=Customer.objects.all()
    return render(request,'admin/viewcustomers.html',{'data1':obj1})
def updatee(request):

    if request.method=='POST':
        cus=Customer.objects.get(id=request.POST.get('cid'))
        cus.email=request.POST.get('mail')
        cus.save()
        obj=Customer.objects.all()
        return viewonecust(request)
        #return render(request,'admin/viewcustomers.html',{'data1':'obj'})

def new(request):
    return render(request,'customer/new.html')


