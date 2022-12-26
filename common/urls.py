from django.urls import path
from . import views
app_name = 'common'

urlpatterns=[
    path('', views.common_index, name='common_index'),
    path('signin', views.common_signin, name='common_signin'),
    path('signup', views.common_signup, name='common_signup'),
    path('faqs', views.common_faqs, name='common_faqs'),
    path('contact', views.common_contact, name='common_contact'),
    # path('home', views.customer_home, name='customer_home'), 

]