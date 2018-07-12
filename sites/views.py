from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sites.forms import LoginForm, RegistrationForm, SignUpform, ForgotPassword

def staticExample(request):

    return render(request, 'sites/static_example.html')


def forgotPassowrd(request):

    form = ForgotPassword()
    message = ''
    if request.method == 'POST':
        form = ForgotPassword(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.get(email = email)
            user.set_password(password)
            user.save()
            message = 'Password reset done successfully!'

    return render(
        request,
        'sites/forgot_password.html',
        {'form': form, 'msg':message}
    )

def userLogin(request):

    if request.user.username:
        return redirect(userDashBoard)

    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                username=username,
                password=password
            )
            if user is None:
                message = 'User not found!'
            else:
                login(request, user)


                return redirect(userDashBoard)

    return render(

        request,
        'sites/login.html',
        {
            'form': form,
            'msg': message
        }
    )


def userDashBoard(request):

    return render(request, 'sites/dashboard.html')

def userLogout(request):

    logout(request)
    return redirect(userLogin)

def userRegistration(request):

    form = SignUpform()
    message = ''
    if request.method == 'POST':
        form = SignUpform(request.POST)
        if form.is_valid():

            user = User()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user.username = username
            user.email = form.cleaned_data['email']
            user.set_password(password)   #password has key
            #user.password = password     #raw password
            user.save()
            message = 'Registration done successfully!'

    return render(
        request,
        'sites/registration.html',
        {'form': form, 'msg': message}
    )