from django.urls import path
from . import views
app_name = 'movieflix_admin'

urlpatterns=[
    path('adminhome', views.admin_home, name='admin_home'), 

]