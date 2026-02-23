
from django.urls import path
from .import views
app_name = 'contact'
urlpatterns = [
path('support',views.FunctionSupport, name='support'),
path('shop',views.FunctionShop,name='shop')
]