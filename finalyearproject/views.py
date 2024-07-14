# <<<<<<< HEAD

import re
from django.shortcuts import render, redirect
from .forms import CameraForm
from django.contrib import messages
import os
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
from .models import TemporaryPerson
from .forms import TemporaryPersonForm
from .forms import AdminUpdateForm
from .models import Attendance
from datetime import datetime
from .forms import EmployeeForm, EmployeeUpdateForm
from .forms import GuardForm, GuardUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
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
    form = EmployeeForm()
    
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
    # Retrieve the previous list of intruder images from the session
    prev_intruder_images = request.session.get('intruder_images', [])
    
    # Get the current list of intruder images
    intruder_images = os.listdir('intruder_images')

    # Get creation timestamps for the images
    timestamps = [datetime.fromtimestamp(os.path.getctime(os.path.join('intruder_images', img))) for img in intruder_images]
    
    # Combine image file names and timestamps into a list of tuples
    intruder_data = zip(intruder_images, timestamps)

    # Check if there are new intruder images
    intruder_detected = set(intruder_images) - set(prev_intruder_images)
    
    # If new intruder images are detected, set a flag to display the message
    if intruder_detected:
        request.session['intruder_images'] = intruder_images
        intruder_detected = True
    else:
        intruder_detected = False

    context = {
        'intruder_data': intruder_data,
        'intruder_detected': intruder_detected
    }
    return render(request, 'adminhome.html', context)
def addcamerapage(request):
    success_message = None
    if request.method == 'POST':
        camera_link = request.POST.get('cameraLink')
        if camera_link.startswith('rtsp'):
            RtspCamera.objects.create(camera_link=camera_link)
            success_message = "Camera link added successfully!"
        else:
            error_message = "Invalid camera link format. Please enter a link starting with 'rtsp'."
            return render(request, 'addcamera.html', {'error_message': error_message})
    return render(request, 'addcamera.html', {'success_message': success_message})
def attendancereportbyadmin(request):
    if request.method == 'POST':
        selected_date = request.POST.get('startDate')
        # Fetch attendance data from the database based on the selected date
        attendance_data = Attendance.objects.filter(date=selected_date)
        # Define an empty list to store formatted attendance data
        formatted_attendance = []
        for attendance in attendance_data:
            # Check if entry time is after 5 am
            if attendance.time.hour >= 5:
                status = 'Absent'
            # Check if entry time is between 8 and 5 am
            elif 8 <= attendance.time.hour < 5:
                status = 'Present'
            else:
                status = 'Unknown'
            # Append formatted data to the list
            formatted_attendance.append({
                'person_id': attendance.person_id,
                'date': attendance.date,
                'time': attendance.time,
                'status': status
            })
        return render(request, 'attendancereport.html', {'attendance_data': formatted_attendance})
    return render(request, 'attendancereport.html')
def registeraccounts(request):
    return render(request,'registeraccount.html')
def regemployee(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Validate ID (username)
        if not username.isdigit():
            messages.error(request, 'ID must be an integer.')
            return render(request, 'registeremployee.html')
        
        if len(username) < 4:
            messages.error(request, 'ID must have 4 or more digits.')
            return render(request, 'registeremployee.html')
        
        # Validate password
        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return render(request, 'registeremployee.html')
        
        if not re.search(r'\d', password):
            messages.error(request, 'Password must contain at least one number.')
            return render(request, 'registeremployee.html')
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            messages.error(request, 'Password must contain at least one special character.')
            return render(request, 'registeremployee.html')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return render(request, 'registeremployee.html')
        
        # Create the new user
        new_user = User.objects.create_user(username=username, password=password)
        employee_group, created = Group.objects.get_or_create(name='employee')
        new_user.groups.add(employee_group)

        messages.success(request, 'Employee account created successfully!')
        return redirect('registeremp')

    return render(request, 'registeremployee.html')
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
    context = {
        'attendance_data': attendance_data  # Pass attendance_data to the template
    }
    return render(request, 'empattendance.html', context)
def guardhome(request):
    # Assuming the Employee model has a field named 'employee_id'
    username = request.user.username
    guard_data = Guard.objects.get(guard_id=username)
    return render(request, 'guardhome.html')
def regguard(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Validate ID (username)
        if not username.isdigit():
            messages.error(request, 'ID must be an integer.')
            return render(request, 'registerguard.html')
        
        if len(username) < 4:
            messages.error(request, 'ID must have 4 or more digits.')
            return render(request, 'registerguard.html')
        
        # Validate password
        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return render(request, 'registerguard.html')
        
        if not re.search(r'\d', password):
            messages.error(request, 'Password must contain at least one number.')
            return render(request, 'registerguard.html')
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            messages.error(request, 'Password must contain at least one special character.')
            return render(request, 'registerguard.html')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return render(request, 'registerguard.html')
        
        # Create the new user
        new_user = User.objects.create_user(username=username, password=password)
        guard_group, created = Group.objects.get_or_create(name='Guard')
        new_user.groups.add(guard_group)
        
        messages.success(request, 'Guard account created successfully!')
        return redirect('registerguard')

    return render(request, 'registerguard.html')
 
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
    else:
        form = GuardForm()

    return render(request, 'addguard.html', {'form': form, 'success_message': success_message})
def guardprofile(request):
    username = request.user.username

    try:
        # Assuming the Employee model has a field named 'employee_id'
        guard_profile = Guard.objects.get(guard_id=username)

        # Your logic for rendering the template with employee_profile

        return render(request, 'guardprofile.html', {'guard_profile': guard_profile})

    except ObjectDoesNotExist:
        # Handle the case where the Employee does not exist
        return render(request, 'guardhome.html', {'error_message': 'Guard profile does not exist.'})
def guardupdate(request):
    username = request.user.username
    guard_profile = Guard.objects.get(guard_id=username)
    if request.method == 'POST':
        form = GuardUpdateForm(request.POST)
        if form.is_valid():
            guard = Guard.objects.get(guard_id=request.user.username)
            guard.phone = form.cleaned_data['phone']
            guard.email = form.cleaned_data['email']
            guard.address = form.cleaned_data['address']
            guard.save()

            
            # return redirect(request, 'empprofile.html', {'employee_profile': employee_profile})
            return redirect('guardprofile')
    else:
        guard = Guard.objects.get(guard_id=request.user.username)
        form = GuardUpdateForm(initial={
            'phone': guard.phone,
            'email': guard.email,
            'address': guard.address,
        })

    return render(request, 'guardprofile.html', {'form': form})
def add_temporary_person(request):
    success_message = None
    error_message = None

    if request.method == 'POST':
        form = TemporaryPersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success_message = "Person added successfully!"
            form = TemporaryPersonForm()  # Reset the form after success
        else:
            error_message = form.errors  # Capture validation errors

    else:
        form = TemporaryPersonForm()

    return render(request, 'tempperson.html', {
        'form': form,
        'success_message': success_message,
        'error_message': error_message,
    })
def temporarypersonadmin(request):
    success_message = None
    error_message = None

    if request.method == 'POST':
        form = TemporaryPersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success_message = "Person added successfully!"
            return render(request, 'temppersonadmin.html', {'success_message': success_message})
        else:
            error_message = form.errors  # Capture validation errors
    else:
        form = TemporaryPersonForm()

    return render(request, 'temppersonadmin.html', {
        'form': form,
        'success_message': success_message,
        'error_message': error_message,
    })
def remove_expired_people():
    expired_people = TemporaryPerson.objects.filter(expiration_datetime__lt=datetime.now())
    for person in expired_people:
        person.photo.delete()
        person.delete()
def adminupdate(request):
    if request.method == 'POST':
        form = AdminUpdateForm(request.POST)
        if form.is_valid():
            admin =Admin.objects.first()
            admin.phone = form.cleaned_data['phone']
            admin.email = form.cleaned_data['email']
            admin.address = form.cleaned_data['address']
            admin.save()
            return redirect('adminprofile')
    else:
        form = AdminUpdateForm(initial={
            'phone': admin.phone,
            'email': admin.email,
            'address': admin.address,
        })

    return render(request, 'adminprofile.html', {'form': form})
def notifications(request):
    intruder_images = os.listdir('intruder_images')
    # Get creation timestamps for the images
    timestamps = [datetime.fromtimestamp(os.path.getctime(os.path.join('intruder_images', img))) for img in intruder_images]
    # Combine image file names and timestamps into a list of tuples
    intruder_data = zip(intruder_images, timestamps)
    return render(request, 'notifications.html', {'intruder_data': intruder_data})
def forgetemp(request):
    return render(request, 'forgetpasswordemp.html')