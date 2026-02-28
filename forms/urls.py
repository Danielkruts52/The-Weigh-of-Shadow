
from django.urls import path
from .import views
app_name = 'form'
urlpatterns = [
    path('vacancydisabled',views.create_vacancy,name='disabled'),
    path('suc',views.Suc,name = 'suc')
]