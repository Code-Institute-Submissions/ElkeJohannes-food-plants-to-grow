from django.shortcuts import render
from .models import Plant, Category


def all_plants(request):
    """ Return the plants overview page """

    plants = Plant.objects.all()
    categories = Category.objects.all()
    
    context = {
        'plants': plants,
        'categories': categories
    }

    return render(request, 'plants/plants.html', context)
    