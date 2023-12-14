from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib import messages
def loginoptions(request):
    return render(request, 'loginas.html')
def loginasadmin(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('adminhomepage')  
        else:
            return render(request, 'loginadmin.html', {'error': 'Invalid login credentials'})
     return render(request,'loginadmin.html')
def loginasemployee(request):
      if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.groups.filter(name='employee').exists():
            login(request, user)
            return redirect('emphome') 
        else:
            return render(request, 'loginemployee.html', {'error': 'Invalid login credentials'})
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
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return render(request, 'registeremployee.html')
        new_user = User.objects.create_user(username=username, password=password)
        employee_group, created = Group.objects.get_or_create(name='employee')
        new_user.groups.add(employee_group)

        messages.success(request, 'Employee account created successfully!')
        return redirect('registeremp')

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