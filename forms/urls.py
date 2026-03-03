from django.urls import path
from . import views

app_name = 'form'

urlpatterns = [
    path('vacancy', views.create_standart_vacancy, name='vacancy'),
    path('young_vacancy', views.create_young_vacancy, name='young'),
    path('vacancydisabled', views.create_vacancy, name='disabled'),
    path('cooperation', views.create_coop, name='coop'),
    path('investor', views.create_investor, name='invest'),
    path('space', views.create_space, name='space'),
    path('suc', views.Suc, name='suc'),
    path('suc/<str:form_type>/', views.Suc, name='suc_with_type'),
]