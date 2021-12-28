from django.shortcuts import render
from .models import Plant, Category


def all_plants(request):
    """ Return the plants overview page """

    categories = Category.objects.all()
    plants = Plant.objects.all()

    if 'category' in request.GET:
        selected_category = request.GET['category']
        plants = Plant.objects.filter(category__name=selected_category)
    
    context = {
        'plants': plants,
        'categories': categories
    }

    return render(request, 'plants/plants.html', context)
