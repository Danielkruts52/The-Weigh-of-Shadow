from django.shortcuts import render
from .models import Form
from .forms import Contactform
from django.contrib import messages

def main(request):
    return render(request, 'myapp/main.html')

def form(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been successfully sent!')
            form = Contactform()
        else:
            messages.error(request, 'The form is filled out incorrectly')
    else:
        form = Contactform()
    
    data = {
        'form': form,
    }
    return render(request, 'myapp/form.html', data)

def Contact(request):
    return render(request, 'myapp/contact.html')

def About(request):
    return render(request, 'myapp/about.html')


