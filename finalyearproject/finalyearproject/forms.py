from django import forms
from .models import Camera
from .models import Employee
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Admin
class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = ['camera_link']
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'employee_id', 'phone', 'email', 'address', 'profile_picture']

    
        