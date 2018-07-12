from django import forms
from crud.models import Employee, Education
from django.core.validators import ValidationError


def checkName(value):

    if value.isdigit():
        raise ValidationError("Name cannot ne digits!")

class EmployeeForm(forms.ModelForm):
    emp_name = forms.CharField(
        max_length=20,
        validators=[checkName]
    )
    address = forms.CharField(
        max_length=250,
        widget=forms.Textarea
    )
    class Meta:
        model = Employee
        fields = '__all__'
        #OR
        #fields = ('emp_email', 'address', 'phone')


#############Different Form For Education #####################

class EducationForm(forms.ModelForm):
    edu_name = forms.CharField(
        max_length=20,

    )
    edu_type = forms.CharField(
        max_length=250,

    )
    edu_uni = forms.CharField(
        max_length=250,
    )

    class Meta:
        model = Education
        fields = '__all__'
