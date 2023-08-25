from django.urls import path
from . import views
app_name = 'customer'

urlpatterns=[
    path('home', views.customer_home, name='customer_home'), 
    path('signout', views.customer_signout, name='customer_signout'),
    path('movie/<int:id>', views.customer_movie, name='customer_movie'),

]