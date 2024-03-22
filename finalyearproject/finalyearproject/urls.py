"""
URL configuration for finalyearproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from .views import employee_list, add_employee
urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.loginoptions, name='loginoptions'),
     path('loginadmin', views.loginasadmin, name='loginasadmin'),
     path('loginemployee', views.loginasemployee, name='loginasemployee'),
     path('loginguard', views.loginasguard, name='loginasguard'),
    path('guardhome', views.guardhome, name='guardhome'),
    
    path('adminhome', views.adminhomepage, name='adminhomepage'),
    path('addcamera', views.addcamerapage, name='addcamerapage'),
    path('attendancereport', views.attendancereportbyadmin, name='attendancereportadmin'),
    path('registeraccount', views.registeraccounts, name='registeracc'),
    path('registeremployee', views.regemployee, name='registeremp'),
    path('registerguard', views.regguard, name='registerguard'),
    path('addperson', views.addperson, name='addper'),
    path('addguard', views.add_Guard, name='addguard'),
    path('employeehome', views.employeehome, name='emphome'),
    path('employeeprofile', views.employeeprofile, name='empprof'),
    path('employeeupdate', views.employeeupdate, name='empupdate'),
     path('guardupdate', views.guardupdate, name='guardupdate'),
    path('guardprofile', views.guardprofile, name='guardprofile'),
    path('notifications', views.notifications, name='notifications'),
    path('employeeattendance', views.employeeatt, name='empattendance'),
    path('connect-camera/', views.connect_camera, name='connect_camera'),
   path('', views.index, name='index'),

	path('livecam_feed', views.livecam_feed, name='livecam_feed'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('add_employee/', views.add_employee, name='addemp'),
      path('adminprofile/', views.adminprofile, name='adminprofile'),
      path('adminupdate/', views.adminupdate, name='adminupdate'),
      path('tempperson/', views.add_temporary_person, name='tempperson'),
      path('temppersonadmin/', views.temporarypersonadmin, name='tempadmin'),
      path('forgetemp', views.forgetemp, name='forgetemp'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


