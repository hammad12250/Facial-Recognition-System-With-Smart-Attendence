# <<<<<<< HEAD


from django.shortcuts import render, redirect
from .forms import CameraForm
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.http.response import StreamingHttpResponse
from django.shortcuts import render
from django.http import StreamingHttpResponse
from finalyearproject.camera import LiveWebCam
from django.shortcuts import render
from .models import RtspCamera
from .models import Employee
from .forms import EmployeeForm
def index(request):
    return render(request, 'adminhome.html')
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
def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def livecam_feed(request):
	return StreamingHttpResponse(gen(LiveWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def add_employee(request):
    success_message = None

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            existing_employee = Employee.objects.filter(employee_id=form.cleaned_data['employee_id']).first()
            if existing_employee:
                messages.error(request, 'Error adding employee. Employee data already exists.')
            else:
                employee = form.save()
                if employee.profile_picture:
                    extension = employee.profile_picture.name.split('.')[-1]
                    new_name = f'{employee.employee_id}.{extension}'
                    employee.profile_picture.name = new_name
                    employee.save()
                success_message = 'Employee added successfully!'
                messages.success(request, success_message)
                return redirect('employee_list')
        else:
            messages.error(request, 'Error adding employee. Please check the form.')
            print(form.errors)
    else:
        form = EmployeeForm()

    return render(request, 'addemployee.html', {'form': form, 'success_message': success_message})


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
    success_message = None
    if request.method == 'POST':
        camera_link = request.POST.get('cameraLink')
        RtspCamera.objects.create(camera_link=camera_link)
        success_message = "Camera link added successfully!"
    return render(request, 'addcamera.html', {'success_message': success_message})
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
def employeehome(request):
     return render(request,'employeehome.html')
def employeeprofile(request):
     return render(request,'empprofile.html')
def employeeupdate(request):
     return render(request,'empupdate.html')