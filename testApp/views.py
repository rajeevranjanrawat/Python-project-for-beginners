from django.shortcuts import render

# Create your views here.

def helloDjango(request):

    return render(request, 'hello.html')

def helloDjango2(request):

    return render(request, 'helllo2.html')