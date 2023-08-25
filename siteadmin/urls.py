from django.urls import path
from . import views
app_name = 'siteadmin'

urlpatterns=[
    path('adminhome', views.admin_home, name='admin_home'), 
    path('signout', views.siteadmin_signout, name='siteadmin_signout'),
    path('movie', views.siteadmin_movie, name='siteadmin_movie'),
    path('customer', views.siteadmin_customer, name='siteadmin_customer'),
    path('delete/<int:id>', views.siteadmin_delete, name='siteadmin_delete'),
    path('addmovie/', views.siteadmin_addmovie, name='siteadmin_addmovie'),
    path('customerdelete/<int:id>', views.siteadmin_customerdelete, name='siteadmin_customerdelete'),
    path('modify/<int:id>', views.siteadmin_modify, name='siteadmin_modify'),


    # path('modify/<int>', views.siteadmin_addmovie, name='siteadmin_addmovie'), 
    # addmovie and modify uses same form and thus same view function. 
    # addmovie for new and modify just need to fetch details and show on the same form
    # by default int = 0 for addmovie and int has other value for modify

]