# <<<<<<< HEAD


from django.shortcuts import render, redirect
from .forms import CameraForm
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.http.response import StreamingHttpResponse
from django.shortcuts import render
from django.http import StreamingHttpResponse
from finalyearproject.camera import LiveWebCam
from django.shortcuts import render

def index(request):
    # Your view logic here
    return render(request, 'adminhome.html')


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


# camera connection starts from here 
def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def livecam_feed(request):
	return StreamingHttpResponse(gen(LiveWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')

# >>>>>>> beda830850716c36d3876ad6a50a748ae81dcc63
# =======
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .models import RtspCamera
# >>>>>>> 17061208419e3c5f98276d9d37d7c4fceac65be7
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
def addemployee(request):
     return render(request,'addemployee.html')
def employeehome(request):
     return render(request,'employeehome.html')
def employeeprofile(request):
     return render(request,'empprofile.html')
def employeeupdate(request):
     return render(request,'empupdate.html')