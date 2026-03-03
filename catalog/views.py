from django.shortcuts import render
from .models import Collections, SpecialCollections, Sweatshirt, T_shirt
def collection(request):
    list_Collections = Collections.objects.all()
    list_SpecialCollections = SpecialCollections.objects.all()
    return render(request, 'catalog/collections.html', {
    'list_Collections': list_Collections,
    'list_SpecialCollections': list_SpecialCollections
})


