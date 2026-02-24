from django.shortcuts import render
from .import views
from .models import Support, shop,office,community
# Create your views here
def FunctionSupport(request):
    list_support = Support.objects.all()
    return render(request, 'contact/support.html',{'list_support':list_support})
def FunctionShop(request):
    list_shop = shop.objects.all()
    return render(request, 'contact/shop.html',{'list_shop':list_shop})
def FunctionOffice(request):
    list_office = office.objects.all()
    return render(request, 'contact/office.html',{'list_office':list_office})
def FunctionCommunity(request):
    list_community = community.objects.all()
    return render(request, 'contact/community.html',{'list_community':list_community})
