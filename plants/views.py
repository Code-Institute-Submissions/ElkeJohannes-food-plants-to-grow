from django.shortcuts import render
from .models import Plant


def all_plants(request):
    """ Return the plants overview page """

    plants = Plant.objects.all()
    
    context = {
        'plants': plants
    }

    return render(request, 'plants/plants.html', context)
    