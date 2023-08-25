from django.shortcuts import render,redirect
from django.contrib import messages
from common.models import Customer
from siteadmin.models import Siteadmin

# Create your views here.

def common_index(request) :
    if request.session.has_key('siteadmin'):
        del request.session['siteadmin']

    elif request.session.has_key('customer'):
        del request.session['customer']
        
    request.session.flush()
    return render(request,'common_templates/index.html')

def common_contact(request):
    return render(request,'common_templates/contact.html')

def common_faqs(request):
    return render(request,'common_templates/faqs.html')

def common_signin(request):
    error_msg = " "
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email_exist = Customer.objects.filter(email = username).exists()
        mobile_exist = Customer.objects.filter(mobile = username).exists()
        admin_exist = Siteadmin.objects.filter(username = username).exists()

        if email_exist : 
            try :         
                customer = Customer.objects.get(email = username, password = password)
                request.session['customer'] = customer.id
                # print(request.session['customer'])
                return redirect('customer:customer_home')
            except:
                error_msg='Username and password does not match'
            
        elif mobile_exist==True :
            try :
                customer = Customer.objects.get(mobile = username, password = password)
                request.session['customer'] = customer.id
                return redirect('customer:customer_home')
            except :
                error_msg='Username and password does not match'

        elif admin_exist : 
            try :         
                siteadmin = Siteadmin.objects.get(username = username, password = password)
                request.session['siteadmin'] = siteadmin.username
                return redirect('siteadmin:admin_home')
            except:
                error_msg='Username and password does not match'
        
        else :
            error_msg = "Username does not Exist"

    return render(request,'common_templates/signin.html',{'error_message':error_msg})

def common_signup(request):
    error_msg = ""
    
    if request.method =='POST':
        # the commented below section is to clear all customers in customer table
        # customer = Customer.objects.all()
        # customer.delete()

        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        email_exist = Customer.objects.filter(email = email).exists()
        if not email_exist:
            if password == c_password:
                customer = Customer(first_name=fname,last_name=lname,email=email,mobile=mobile,password=password)
                customer.save()
                messages.success(request,"Your Account has been successfully created")
                return redirect('common:common_signin')
            else:
                error_msg = "passwords do not match"
        else:
            error_msg = "Email already exists!"

    return render(request,'common_templates/signup.html',{'message':error_msg})








# def customer_home(request):
#     return render(request,'customer_templates/home.html')



# def customer_home(request):
#     return render(request,'common_templates/home.html')
