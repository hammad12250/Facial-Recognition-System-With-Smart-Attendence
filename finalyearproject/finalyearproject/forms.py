from django import forms
from .models import Camera
from .models import Admin
from .models import Employee
from .models import Guard
from .models import TemporaryPerson
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
class GuardForm(forms.ModelForm):
    class Meta:
        model = Guard
        fields = ['name', 'guard_id', 'phone', 'email', 'address', 'profile_picture']
    def clean_guard_id(self):
        guard_id = self.cleaned_data['guard_id']

        # Ensure that guard_id is an integer
        try:
            int(guard_id)
        except ValueError:
            raise forms.ValidationError("Guard ID must be an integer.")

        return guard_id

    def clean_email(self):
        email = self.cleaned_data['email']

        # Ensure that email ends with '@gmail.com'
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email must be in the form of '@gmail.com'.")

        return email
class GuardUpdateForm(forms.Form):
    phone = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)
class TemporaryPersonForm(forms.ModelForm):
    class Meta:
        model = TemporaryPerson
        fields = ['name', 'person_id','reason_for_visiting', 'expiration_datetime', 'photo']
class AdminUpdateForm(forms.Form):
    phone = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)