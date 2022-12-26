from django.shortcuts import render

# Create your views here.

def common_index(request):
    return render(request,'common_templates/index.html')

def common_contact(request):
    return render(request,'common_templates/contact.html')

def common_faqs(request):
    return render(request,'common_templates/faqs.html')

def common_signin(request):
    return render(request,'common_templates/signin.html')

def common_signup(request):
    return render(request,'common_templates/signup.html')

# def customer_home(request):
#     return render(request,'common_templates/home.html')
