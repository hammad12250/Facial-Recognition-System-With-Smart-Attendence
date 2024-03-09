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
from .models import Employee, Attendance
from .models import Admin
from .models import Guard
from .forms import EmployeeForm, EmployeeUpdateForm
from .forms import GuardForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
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
                form.save()
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

        # Check if the username is not empty
        if not username:
            messages.error(request, 'Please enter a valid username.')
            return render(request, 'loginemployee.html', {'error': 'Please enter a valid username.'})

        # Check if a user with the given username exists
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')
            return render(request, 'loginemployee.html', {'error': 'User does not exist.'})

        # Authenticate the user after verifying existence
        user = authenticate(request, username=username, password=password)

        if user is not None and user.groups.filter(name='employee').exists():
            login(request, user)
            return redirect('emphome') 
        else:
            messages.error(request, 'Invalid login credentials.')
            return render(request, 'loginemployee.html', {'error': 'Invalid login credentials.'})

    return render(request, 'loginemployee.html')
def loginasguard(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username is not empty
        if not username:
            messages.error(request, 'Please enter a valid username.')
            return render(request, 'loginguard.html', {'error': 'Please enter a valid username.'})

        # Check if a user with the given username exists
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')
            return render(request, 'loginguard.html', {'error': 'User does not exist.'})

        # Authenticate the user after verifying existence
        user = authenticate(request, username=username, password=password)

        if user is not None and user.groups.filter(name='Guard').exists():
            login(request, user)
            return redirect('guardhome') 
        else:
            messages.error(request, 'Invalid login credentials.')
            return render(request, 'loginguard.html', {'error': 'Invalid login credentials.'})

    return render(request, 'loginguard.html')
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
@csrf_protect
def employeehome(request):
    # Assuming the Employee model has a field named 'employee_id'
    username = request.user.username
    employee_data = Employee.objects.get(employee_id=username)
    attendance_data = Attendance.objects.filter(person_id=username)

    return render(request, 'employeehome.html', {'employee_data': employee_data, 'attendance_data': attendance_data})
    # return render(request, 'employeehome.html', {'employee_data': employee_data})
@csrf_protect
def employeeprofile(request):
    username = request.user.username

    try:
        # Assuming the Employee model has a field named 'employee_id'
        employee_profile = Employee.objects.get(employee_id=username)

        # Your logic for rendering the template with employee_profile

        return render(request, 'empprofile.html', {'employee_profile': employee_profile})

    except ObjectDoesNotExist:
        # Handle the case where the Employee does not exist
        return render(request, 'employeehome.html', {'error_message': 'Employee profile does not exist.'})

def employeeupdate(request):
    username = request.user.username
    employee_profile = Employee.objects.get(employee_id=username)
    if request.method == 'POST':
        form = EmployeeUpdateForm(request.POST)
        if form.is_valid():
            # Update the employee details in the database
            employee = Employee.objects.get(employee_id=request.user.username)
            employee.phone = form.cleaned_data['phone']
            employee.email = form.cleaned_data['email']
            employee.address = form.cleaned_data['address']
            employee.save()

            
            # return redirect(request, 'empprofile.html', {'employee_profile': employee_profile})
            return redirect('empprof')
    else:
        employee = Employee.objects.get(employee_id=request.user.username)
        form = EmployeeUpdateForm(initial={
            'phone': employee.phone,
            'email': employee.email,
            'address': employee.address,
        })

    return render(request, 'empprofile.html', {'form': form})
def adminprofile(request):
    adminprofile = Admin.objects.first()
    return render(request, 'adminprofile.html', {'adminprofile': adminprofile})
def employeeatt(request):
    # Fetch attendance data from the database
    username = request.user.username
    employee_data = Employee.objects.get(employee_id=username)
    attendance_data = Attendance.objects.filter(person_id=username)
    return render(request, 'empattendance.html')
def guardhome(request):
    # Assuming the Employee model has a field named 'employee_id'
    username = request.user.username
    guard_data = Guard.objects.get(guard_id=username)
    return render(request, 'guardhome.html')
def regguard(request):
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return render(request, 'registerguard.html')
        new_user = User.objects.create_user(username=username, password=password)
        Guard_group, created = Group.objects.get_or_create(name='Guard')
        new_user.groups.add(Guard_group)
        messages.success(request, 'Guard account created successfully!')
        return redirect('registerguard')
     return render(request,'registerGuard.html')  
 
def add_Guard(request):
    success_message = None
    if request.method == 'POST':
        form = GuardForm(request.POST, request.FILES)
        if form.is_valid():
            existing_guard = Guard.objects.filter(guard_id=form.cleaned_data['guard_id']).first()
            if existing_guard:
                messages.error(request, 'Error adding guard. Guard data already exists.')
            else:
                form.save()
                success_message = 'Guard added successfully!'
                messages.success(request, success_message)
                return redirect('addguard')
        else:
            messages.error(request, 'Error adding guard. Please check the form.')
            print(form.errors)
    else:
        form = GuardForm()

    return render(request, 'addguard.html', {'form': form, 'success_message': success_message})