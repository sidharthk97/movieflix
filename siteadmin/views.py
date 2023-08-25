from django.shortcuts import render, redirect

from .models import Movie
from common.models import Customer

# Create your views here.


def admin_home(request):
    return render(request,'admin_templates/adminhome.html')

def siteadmin_signout(request):
    
    del request.session['siteadmin']
    request.session.flush()
    return redirect('common:common_index')

def siteadmin_movie(request):
    movielist = Movie.objects.all()
    return render(request,'admin_templates/movielist.html',{'movielist':movielist})

def siteadmin_customer(request):
    customerlist = Customer.objects.all()
    return render(request,'admin_templates/customerlist.html',{'customerlist':customerlist})

def siteadmin_addmovie(request):
    id = request.GET.get('id','')
   
    error_msg = ""
    if request.method =='GET':   

        if id =="":
            return render(request,'admin_templates/addmovie.html')
        else :
            
            movie = Movie.objects.get(id=id)
            return render(request,'admin_templates/addmovie.html',{'movie':movie})
    elif request.method == "POST" :
        # when method = post
        if id == "":
            print("inside if ",id)
            name = request.POST.get('name')
            language = request.POST.get('language')
            category = request.POST.get('category')
            year = request.POST.get('year')
            pic = request.FILES['pic']
            video = request.FILES['video']

            movie_exist = Movie.objects.filter(name = name, language = language).exists()
            if not movie_exist :
                movie = Movie(name=name, language=language, category=category, year=year, pic=pic, video=video)
                movie.save()
                return render(request,'admin_templates/adminhome.html')
            else :
                error_msg = "Movie in same language already exists"

            return render(request,'admin_templates/addmovie.html', {'error_message':error_msg})
        
        else :
            print("inside if else ",id)     
            name = request.POST.get('name')
            language = request.POST.get('language')
            category = request.POST.get('category')
            year = request.POST.get('year')
            pic = request.FILES['pic']
            video = request.FILES['video']

            # movie = Movie.objects.get(id=id)
            # movie = Movie.objects.filter(id=id).update(name=name, language=language, category=category, year=year, pic=pic, video=video)
            movie = Movie.objects.get(id=id)
            movie.name=name
            movie.language=language
            movie.category=category
            movie.year=year 
            movie.pic=pic
            movie.video=video
            movie.save()
            return redirect('siteadmin:siteadmin_movie')
            # return render(request,'admin_templates/addmovie.html',{'movie':movie})

def siteadmin_delete(request,id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('siteadmin:siteadmin_movie')

def siteadmin_customerdelete(request,id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('siteadmin:siteadmin_customer')

def customer_home(request):
    customer = Customer.objects.get(id = request.session['customer'])   
    return render(request,'customer_templates/home.html',{'customer':customer})

def siteadmin_modify(request, id):
    if request.method =='GET':   
        customer = Customer.objects.get(id=id)
        return render(request,'admin_templates/customer_modify.html',{'customer':customer})
    
    elif request.method == "POST" :
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
       
        Customer.objects.filter(id=id).update(first_name=first_name, last_name = last_name, mobile = mobile, email = email, password = password)
        return redirect('siteadmin:siteadmin_customer')

    

