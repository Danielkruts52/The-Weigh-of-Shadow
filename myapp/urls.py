
from django.urls import path
from .import views
urlpatterns = [
   path('',views.main, name='main'),
   path('form', views.form, name = 'form'),
   path('contact',views.Contact,name = 'contact'),
   path('about', views.About, name = 'about')
]