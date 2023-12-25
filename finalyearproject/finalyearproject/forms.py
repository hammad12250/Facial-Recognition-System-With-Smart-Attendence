from django import forms
from .models import Camera
from .models import Employee
class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = ['camera_link']
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'employee_id', 'phone', 'email', 'address', 'profile_picture']

class EmployeeUpdateForm(forms.Form):
    phone = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)