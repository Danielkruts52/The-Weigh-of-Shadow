from django.shortcuts import render

def collection(request):
    return render(request, 'catalog/collections.html')
