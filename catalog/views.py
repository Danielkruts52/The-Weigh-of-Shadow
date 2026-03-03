from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Collections, SpecialCollections, Sweatshirt, T_shirt

def collection(request):
    """Главная страница со всеми коллекциями"""
    list_Collections = Collections.objects.all()
    list_SpecialCollections = SpecialCollections.objects.all()
    
    context = {
        'list_Collections': list_Collections,
        'list_SpecialCollections': list_SpecialCollections,
    }
    return render(request, 'catalog/collections.html', context)

def collection_detail(request, collection_name):
    """Детальная страница обычной коллекции со всеми товарами"""
    # Получаем информацию о коллекции
    collection = get_object_or_404(Collections, name=collection_name)
    
    # Получаем все товары этой коллекции
    t_shirts = T_shirt.objects.filter(collections_type=collection_name)
    sweatshirts = Sweatshirt.objects.filter(collections_type=collection_name)
    
    # Находим минимальную и максимальную цену для фильтра
    all_prices = []
    items = []
    
    for t_shirt in t_shirts:
        # Обработка строки цены
        price_str = t_shirt.price
        # Убираем пробелы, заменяем запятую на точку, убираем $
        price_str = price_str.replace(' ', '').replace(',', '.').replace('$', '')
        price = float(price_str)
        
        all_prices.append(price)
        items.append({
            'id': t_shirt.id,
            'type': 't-shirt',
            'name': t_shirt.name,
            'image': t_shirt.image,
            'image2': t_shirt.image2,
            'structure': t_shirt.structure,
            'price': price,
            'text': t_shirt.text,
            "get_absolute_url": t_shirt.get_absolute_url
        })
    
    for sweatshirt in sweatshirts:
        # Обработка строки цены
        price_str = sweatshirt.price
        # Убираем пробелы, заменяем запятую на точку, убираем $
        price_str = price_str.replace(' ', '').replace(',', '.').replace('$', '')
        price = float(price_str)
        
        all_prices.append(price)
        items.append({
            'id': sweatshirt.id,
            'type': 'sweatshirt',
            'name': sweatshirt.name,
            'image': sweatshirt.image,
            'image2': sweatshirt.image2,
            'structure': sweatshirt.structure,
            'price': price,
            'text': sweatshirt.text,
            "get_absolute_url": sweatshirt.get_absolute_url,
        })
    
    min_price = min(all_prices) if all_prices else 0
    max_price = max(all_prices) if all_prices else 1000
    
    context = {
        'collection': collection,
        'items': items,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'catalog/collection_detail.html', context)

def special_collection_detail(request, collection_name):
    """Детальная страница специальной коллекции со всеми товарами"""
    # Получаем информацию о специальной коллекции
    collection = get_object_or_404(SpecialCollections, name=collection_name)
    
    # Получаем все товары этой коллекции
    t_shirts = T_shirt.objects.filter(collections_type=collection_name)
    sweatshirts = Sweatshirt.objects.filter(collections_type=collection_name)
    
    # Находим минимальную и максимальную цену для фильтра
    all_prices = []
    items = []
    
    for t_shirt in t_shirts:
        # Обработка строки цены
        price_str = t_shirt.price
        # Убираем пробелы, заменяем запятую на точку, убираем $
        price_str = price_str.replace(' ', '').replace(',', '.').replace('$', '')
        price = float(price_str)
        
        all_prices.append(price)
        items.append({
            'id': t_shirt.id,
            'type': 't-shirt',
            'name': t_shirt.name,
            'image': t_shirt.image,
            'image2': t_shirt.image2,
            'structure': t_shirt.structure,
            'price': price,
            'text': t_shirt.text,
        })
    
    for sweatshirt in sweatshirts:
        # Обработка строки цены
        price_str = sweatshirt.price
        # Убираем пробелы, заменяем запятую на точку, убираем $
        price_str = price_str.replace(' ', '').replace(',', '.').replace('$', '')
        price = float(price_str)
        
        all_prices.append(price)
        items.append({
            'id': sweatshirt.id,
            'type': 'sweatshirt',
            'name': sweatshirt.name,
            'image': sweatshirt.image,
            'image2': sweatshirt.image2,
            'structure': sweatshirt.structure,
            'price': price,
            'text': sweatshirt.text,
        })
    
    min_price = min(all_prices) if all_prices else 0
    max_price = max(all_prices) if all_prices else 1000
    
    context = {
        'collection': collection,
        'items': items,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'catalog/special_collection_detail.html', context)

def t_shirt_detail(request, item_id):
    """Детальная страница конкретной футболки"""
    t_shirt = get_object_or_404(T_shirt, id=item_id)
    
    # Обработка цены
    price_str = t_shirt.price
    price_str = price_str.replace(' ', '').replace(',', '.').replace('$', '')
    t_shirt.price_numeric = float(price_str)
    
    # Получаем информацию о коллекции этой футболки
    try:
        collection = Collections.objects.get(name=t_shirt.collections_type)
        collection_type = 'regular'
    except Collections.DoesNotExist:
        try:
            collection = SpecialCollections.objects.get(name=t_shirt.collections_type)
            collection_type = 'special'
        except SpecialCollections.DoesNotExist:
            collection = None
            collection_type = None
    
    # Получаем похожие товары из той же коллекции
    similar_items = T_shirt.objects.filter(
        collections_type=t_shirt.collections_type
    ).exclude(id=item_id)[:4]
    
    # Обрабатываем цены для похожих товаров
    for item in similar_items:
        price_str = item.price
        price_str = price_str.replace(' ', '').replace(',', '.').replace('$', '')
        item.price_numeric = float(price_str)
    
    similar_sweatshirts = Sweatshirt.objects.filter(
        collections_type=t_shirt.collections_type
    )[:2]
    
    # Обрабатываем цены для похожих толстовок
    for item in similar_sweatshirts:
        price_str = item.price
        price_str = price_str.replace(' ', '').replace(',', '.').replace('$', '')
        item.price_numeric = float(price_str)
    
    context = {
        'item': t_shirt,
        'item_type': 't-shirt',
        'collection': collection,
        'collection_type': collection_type,
        'similar_items': similar_items,
        'similar_sweatshirts': similar_sweatshirts,
    }
    return render(request, 'catalog/item_detail.html', context)

def sweatshirt_detail(request, item_id):
    """Детальная страница конкретной толстовки"""
    sweatshirt = get_object_or_404(Sweatshirt, id=item_id)
    
    # Обработка цены
    price_str = sweatshirt.price
    price_str = price_str.replace(' ', '').replace(',', '.').replace('$', '')
    sweatshirt.price_numeric = float(price_str)
    
    # Получаем информацию о коллекции этой толстовки
    try:
        collection = Collections.objects.get(name=sweatshirt.collections_type)
        collection_type = 'regular'
    except Collections.DoesNotExist:
        try:
            collection = SpecialCollections.objects.get(name=sweatshirt.collections_type)
            collection_type = 'special'
        except SpecialCollections.DoesNotExist:
            collection = None
            collection_type = None
    
    # Получаем похожие товары из той же коллекции
    similar_items = Sweatshirt.objects.filter(
        collections_type=sweatshirt.collections_type
    ).exclude(id=item_id)[:4]
    
    # Обрабатываем цены для похожих товаров
    for item in similar_items:
        price_str = item.price
        price_str = price_str.replace(' ', '').replace(',', '.').replace('$', '')
        item.price_numeric = float(price_str)
    
    similar_t_shirts = T_shirt.objects.filter(
        collections_type=sweatshirt.collections_type
    )[:2]
    
    # Обрабатываем цены для похожих футболок
    for item in similar_t_shirts:
        price_str = item.price
        price_str = price_str.replace(' ', '').replace(',', '.').replace('$', '')
        item.price_numeric = float(price_str)
    
    context = {
        'item': sweatshirt,
        'item_type': 'sweatshirt',
        'collection': collection,
        'collection_type': collection_type,
        'similar_items': similar_items,
        'similar_t_shirts': similar_t_shirts,
    }
    return render(request, 'catalog/item_detail.html', context)