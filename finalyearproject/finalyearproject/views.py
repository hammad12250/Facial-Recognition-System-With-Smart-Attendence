from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from .forms import CameraForm
from django.contrib import messages
# camera connect storing data in database


def connect_camera(request):
    if request.method == 'POST':
        form = CameraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Camera successfully connected.')
            return redirect('connect_camera')  # Redirect to the same page to display the success message
    else:
        form = CameraForm()

    return render(request, 'addcamera.html', {'form': form})

def loginoptions(request):
    return render(request, 'loginas.html')
def loginasadmin(request):
    return render(request,'loginadmin.html')
def loginasemployee(request):
    return render(request,'loginemployee.html')
def loginasguard(request):
    return render(request,'loginguard.html')
def adminhomepage(request):
    return render(request,'adminhome.html')
def addcamerapage(request):
    return render(request,'addcamera.html')
def attendancereportbyadmin(request):
    return render(request,'attendancereport.html')
def registeraccounts(request):
    return render(request,'registeraccount.html')
def regemployee(request):
     return render(request,'registeremployee.html')
def addperson(request):
     return render(request,'addperson.html')
def addemployee(request):
     return render(request,'addemployee.html')
def employeehome(request):
     return render(request,'employeehome.html')
def employeeprofile(request):
     return render(request,'empprofile.html')
def employeeupdate(request):
     return render(request,'empupdate.html')