from django.shortcuts import render, redirect
from crud.forms import EmployeeForm, EducationForm
from crud.models import Employee, Education
from django.contrib.auth.decorators import login_required
from django.views import View

############################## AJAX  ##############################################


####################################################################################3
class CreateView(View):

    def get(self, request):
        form = EmployeeForm()
        return render(request, 'crud/create.html', {'form': form})


    def post(self, request):

        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
        return render(request, 'crud/create.html', {'form': form})


# Create your views here.

def create(request):

    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
           emp = Employee()
           empName = form.cleaned_data['emp_email'].split('@')[0]
           emp.emp_name = empName
           emp.emp_email = form.cleaned_data['emp_email']
           emp.address = form.cleaned_data['address']
           emp.phone = form.cleaned_data['phone']
           emp.save()
           return redirect(index)
            #form.save()         #API CALL

    return render(request, 'crud/create.html', {'form': form})

@login_required(login_url='/sites/signin')   #decorator
def index(request):

    resultSet = Employee.objects.all()
    #resultSet = Employee.objects.filter().order_by('-id')
    #resultSet = Employee.objects.raw("select * from employee where emp_name='rajeev'")

    return render(request, 'crud/index.html', {'data': resultSet})

def update(request, id):

    data = Employee.objects.get(id=id)
    #select * from employee where id = id
    form = EmployeeForm(instance=data)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=data)
        if form.is_valid():
            emp = Employee()
            emp.id = id
            empName = form.cleaned_data['emp_name'] #to fetch from Email ID we can add this --> .split('@')[0]
            emp.emp_name = empName
            emp.emp_email = form.cleaned_data['emp_email']
            emp.address = form.cleaned_data['address']
            emp.phone = form.cleaned_data['phone']
            emp.save()
            return redirect(index)
            # form.save()         #API CALL
    return render(request, 'crud/update.html', {'form': form})

def delete(request, id):

    data = Employee.objects.get(id=id)
    data.delete()
    return redirect(index)

def view(request, id):

    data = Employee.objects.get(id=id)
    return render(request, 'crud/view.html', {'data': data})

#########################DIFFERENT TABLE##########################################

def create2(request):

    form = EducationForm()
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():

            edu = Education()

            edu.edu_name = form.cleaned_data['edu_name']
            edu.employee = form.cleaned_data['employee']
            edu.edu_type = form.cleaned_data['edu_type']
            edu.edu_uni = form.cleaned_data['edu_uni']
            edu.save()
        return redirect(index2)
            #form.save()         #API CALL

    return render(request, 'crud/education.html', {'form': form})

def index2(request):

    resultSet = Education.objects.all()
    return render(request, 'crud/edu_index.html', {'data': resultSet})
