from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DisabilityVacancyForm, VacancyForm, YoungVacancyForm, SpaceForm, InvestorForm, cooperationForm

def Suc(request, form_type=None):
    # Словарь для сопоставления типов форм с их названиями
    form_names = {
        'standart': 'Standard vacancy',
        'young': 'Youth Program',
        'disability': 'For people with disabilities',
        'space': 'space',
        'investor': 'Investor',
        'cooperation': 'Cooperation',
    }
    
    # Словарь для сопоставления типов форм с URL для возврата
    return_urls = {
        'standart': 'form:vacancy',
        'young': 'form:young',
        'disability': 'form:disabled',
        'space': 'form:space',
        'investor': 'form:invest',
        'cooperation': 'form:coop',
    }
    
    # Получаем название формы или значение по умолчанию
    form_display_name = form_names.get(form_type, 'Форма')
    return_url = return_urls.get(form_type, 'form:disabled')
    
    return render(request, 'forms_/success.html', {
        'form_type': form_type,
        'form_display_name': form_display_name,
        'return_url': return_url
    })

def create_standart_vacancy(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your RESUME has been successfully submitted!')
            return redirect('form:suc_with_type', form_type='standart')
        else:
            # Для отладки
            print("Form errors:", form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = VacancyForm()
    
    return render(request, 'forms_/standart_vacancy.html', {'form': form})

def create_young_vacancy(request):
    if request.method == 'POST':
        form = YoungVacancyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your RESUME has been successfully submitted!')
            return redirect('form:suc_with_type', form_type='young')
        else:
            # Для отладки
            print("Form errors:", form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = YoungVacancyForm()
    
    return render(request, 'forms_/young_vacancy.html', {'form': form})

def create_vacancy(request):
    if request.method == 'POST':
        form = DisabilityVacancyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your RESUME has been successfully submitted!')
            return redirect('form:suc_with_type', form_type='disability')
        else:
            # Для отладки
            print("Form errors:", form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = DisabilityVacancyForm()
    
    return render(request, 'forms_/vacancy_form.html', {'form': form})

def create_space(request):
    if request.method == 'POST':
        form = SpaceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your RESUME has been successfully submitted!')
            return redirect('form:suc_with_type', form_type='space')
        else:
            # Для отладки
            print("Form errors:", form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SpaceForm()
    
    return render(request, 'forms_/space.html', {'form': form})

def create_investor(request):
    if request.method == 'POST':
        form = InvestorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your RESUME has been successfully submitted!')
            return redirect('form:suc_with_type', form_type='investor')
        else:
            # Для отладки
            print("Form errors:", form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = InvestorForm()
    
    return render(request, 'forms_/investor.html', {'form': form})

def create_coop(request):
    if request.method == 'POST':
        form = cooperationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your RESUME has been successfully submitted!')
            return redirect('form:suc_with_type', form_type='cooperation')
        else:
            # Для отладки
            print("Form errors:", form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = cooperationForm()
    
    return render(request, 'forms_/com.html', {'form': form})