from django.urls import path
from . import views
app_name = 'collections'
urlpatterns = [
    path('collections',views.collection, name ='collec')
]