
from django.urls import path
from .import views
app_name = 'form'
urlpatterns = [
    path('vacancy', views.create_standart_vacancy,name='vacancy'),
    path('young_vacancy',views.create_young_vacancy,name = 'young'),
    path('vacancydisabled',views.create_vacancy,name='disabled'),
    path('suc',views.Suc,name = 'suc')
]