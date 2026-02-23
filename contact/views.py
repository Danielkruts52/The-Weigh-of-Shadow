from django.shortcuts import render
from .import views
from .models import Support, shop
# Create your views here
def FunctionSupport(request):
    list_support = Support.objects.all()
    return render(request, 'contact/support.html',{'list_support':list_support})
def FunctionShop(request):
    list_shop = shop.objects.all()
    return render(request, 'contact/shop.html',{'list_shop':list_shop})