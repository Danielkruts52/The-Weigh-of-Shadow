from django.shortcuts import render
from .models import Event

def EventFunction(request):
    list_event = Event.objects.all()
    return render(request, 'community/community.html', {'list_event':list_event})
