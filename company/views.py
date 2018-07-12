from django.shortcuts import render

# Create your views here.

def hellocompany(request):

    d1 = {
        'name':'rajeev',
        'email':'rajeev@agmail.com',
        'l1': [1, 2, 3, 4, 5],
        'd2': {'city':'Bangaore', 'Address':'BTM'}

    }
    return render(request, 'company.html', d1)
