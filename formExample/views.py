from django.shortcuts import render
from formExample.forms import FormExample

# Create your views here.

def formExample(request):

    form = FormExample()
    if request.method == 'POST':
        form = FormExample(request.POST) # request.POST will capture all the form data
        if form.is_valid():
            pass

    d1 = {
        'form': form
    }
    return render(request, 'form.html', d1)
