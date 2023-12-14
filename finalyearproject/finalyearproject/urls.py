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
from .views import connect_camera
urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.loginoptions, name='loginoptions'),
     path('loginadmin', views.loginasadmin, name='loginasadmin'),
     path('loginemployee', views.loginasemployee, name='loginasemployee'),
     path('loginguard', views.loginasguard, name='loginasguard'),
    path('adminhome', views.adminhomepage, name='adminhomepage'),
    path('addcamera', views.addcamerapage, name='addcamerapage'),
    path('attendancereport', views.attendancereportbyadmin, name='attendancereportadmin'),
    path('registeraccount', views.registeraccounts, name='registeracc'),
    path('registeremployee', views.regemployee, name='registeremp'),
    path('addperson', views.addperson, name='addper'),
    path('addemployee', views.addemployee, name='addemp'),
    path('employeehome', views.employeehome, name='emphome'),
    path('employeeprofile', views.employeeprofile, name='empprof'),
    path('employeeupdate', views.employeeupdate, name='empupdate'),
    path('connect-camera/', connect_camera, name='connect_camera'),
    
]


