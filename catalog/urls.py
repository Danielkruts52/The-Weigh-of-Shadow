from django.urls import path
from . import views

app_name = 'collections'

urlpatterns = [
    # Главная страница со всеми коллекциями
    path('collections/', views.collection, name='collec'),
    
    # Страницы обычных коллекций
    path('collection/<str:collection_name>/', views.collection_detail, name='collection_detail'),
    
    # Страницы специальных коллекций
    path('special-collection/<str:collection_name>/', views.special_collection_detail, name='special_collection_detail'),
    
    # Детальные страницы товаров
    path('t-shirt/<int:item_id>/', views.t_shirt_detail, name='t_shirt_detail'),
    path('sweatshirt/<int:item_id>/', views.sweatshirt_detail, name='sweatshirt_detail'),
]