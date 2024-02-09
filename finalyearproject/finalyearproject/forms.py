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
    def clean_employee_id(self):
        employee_id = self.cleaned_data['employee_id']

        # Ensure that employee_id is an integer
        try:
            int(employee_id)
        except ValueError:
            raise forms.ValidationError("Employee ID must be an integer.")

        return employee_id

    def clean_email(self):
        email = self.cleaned_data['email']

        # Ensure that email ends with '@gmail.com'
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email must be in the form of '@gmail.com'.")

        return email
class EmployeeUpdateForm(forms.Form):
    phone = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)