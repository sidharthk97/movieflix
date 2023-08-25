from django.shortcuts import render, redirect

from common.models import Customer
from siteadmin.models import Movie
# from .decorators import auth_customer

# Create your views here.

# @auth_customer
def customer_home(request):
    customer = Customer.objects.get(id = request.session['customer'])   
    movielist = Movie.objects.all()
    return render(request,'customer_templates/home.html',{'customer':customer, 'movielist':movielist})

def customer_signout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('common:common_index')

def customer_movie(request,id):
    customer = Customer.objects.get(id = request.session['customer']) 
    movie = Movie.objects.get(id = id)   
    return render(request,'customer_templates/movie.html',{'movie':movie,'customer':customer})