from django.shortcuts import render
from .models import Support, shop, office, community  # Убрал лишний .import views

# Create your views here
def FunctionSupport(request):
    # Получаем все объекты Support
    list_support = Support.objects.all()
    
    # Проверяем, есть ли параметр фильтра в GET запросе
    selected_country = request.GET.get('country')
    
    # Применяем фильтр, если страна выбрана
    if selected_country and selected_country in ['USA', 'CA']:
        list_support = list_support.filter(type=selected_country)
    
    # Передаем выбранную страну в шаблон для отображения активного фильтра
    context = {
        'list_support': list_support,
        'selected_country': selected_country,
    }
    return render(request, 'contact/support.html', context)

def FunctionShop(request):
    list_shop = shop.objects.all()
    return render(request, 'contact/shop.html', {'list_shop': list_shop})

def FunctionOffice(request):
    list_office = office.objects.all()
    return render(request, 'contact/office.html', {'list_office': list_office})

def FunctionCommunity(request):
    list_community = community.objects.all()
    return render(request, 'contact/community.html', {'list_community': list_community})