from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DisabilityVacancyForm

def Suc(request):
    return render(request, 'forms_/success.html')

def create_vacancy(request):
    if request.method == 'POST':
        form = DisabilityVacancyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your RESUME has been successfully submitted!')
            return redirect('form:suc')
        else:
            # Для отладки
            print("Form errors:", form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = DisabilityVacancyForm()
    
    return render(request, 'forms_/vacancy_form.html', {'form': form})