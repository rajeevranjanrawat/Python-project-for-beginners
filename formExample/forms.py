from django import forms
from django.core.validators import ValidationError

#def validateName(value):

#    if value.isdigit():
 #       raise ValidationError(" user name cannot be in Digits")

#def validateEmail(value):

   # temp = email.split('@')[1]
   # if temp != '@mytectra.com':

#    if value.find('@mytectra.com') == -1:
 #       raise ValidationError("Invalid Email ID(@mytectra.com)")

class FormExample(forms.Form):

    cityList = (
                ('','--Select Option--'),
                ('chennai', 'Chennai'),
                ('bangaore', 'Bangalore'),
                ('hyderabad', 'Hyderabad'),
                ('mysore', 'Mysore')
                )
    gn = (
        ('m','Male'),
        ('f','Female')
    )

    city = forms.ChoiceField(
                            choices=cityList
                            )

    gender = forms.ChoiceField(
        choices=gn, widget=forms.RadioSelect
    )

    is_active = forms.BooleanField(required=False)

    username = forms.CharField(min_length=8, max_length=20, required= False, label='Name', help_text= "Please provide valid user name",
                               error_messages={
                                   'required': "Employee name cannot blank",'min_length':'new Text'
                               },
                               #validators=[validateName],
                               widget=forms.TextInput(
                                   attrs={
                                       'placeholder':'Employee name',
                                       'class':'text',
                                       'id':'qqqq'
                                   }
                               )

                               )

    email = forms.EmailField()
    address = forms.CharField(
                                max_length=250,
                                widget=forms.Textarea
                                )

    password1 = forms.CharField(
                                max_length=100,
                                widget=forms.PasswordInput
                                )

    password2 = forms.CharField(
                                max_length=100,
                                widget=forms.PasswordInput
                                )

    def clean(self):

        form_data = self.cleaned_data

        if 'username' in form_data:
            if form_data['username'].isdigit():
                self.errors['username'] = ['Employee name cannot be digits']

        if 'email' in form_data:
            if form_data['email'].find('@mytectra.com')<0:
                self.errors['email'] = ['Invalid Email']

        if 'password1' in form_data and 'password2' in form_data:
            if form_data['password1'] != form_data['password2']:
                self.errors['password2'] = ['password mismatch']

        return form_data
