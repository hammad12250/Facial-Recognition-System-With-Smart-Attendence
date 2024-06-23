from django import forms
from .models import Camera
from .models import Admin
from .models import Employee
from .models import Guard
from .models import TemporaryPerson
from django.core.exceptions import ValidationError
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

        # Ensure that employee_id is an integer with at least 4 digits
        try:
            employee_id_int = int(employee_id)
            if len(str(employee_id_int)) < 4:
                raise forms.ValidationError("Employee ID must have at least 4 digits.")
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

       # Ensure that employee_id is an integer with at least 4 digits
        try:
            guard_id_int = int(guard_id)
            if len(str(guard_id_int)) < 4:
                raise forms.ValidationError("Guard ID must have at least 4 digits.")
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
        fields = ['name', 'person_id', 'reason_for_visiting', 'expiration_datetime', 'photo']
        widgets = {
            'expiration_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean_person_id(self):
        person_id = self.cleaned_data.get('person_id')

        if not str(person_id).isdigit():
            raise ValidationError('Person ID must be an integer.')

        if len(str(person_id)) < 4:
            raise ValidationError('Person ID must be at least 4 digits long.')

        if TemporaryPerson.objects.filter(person_id=person_id).exists():
            raise ValidationError('Person ID already exists.')

        return person_id
class AdminUpdateForm(forms.Form):
    phone = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)