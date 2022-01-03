from django.shortcuts import render, get_object_or_404
from .models import Plant, Category
from django.db.models import Q

def all_plants(request):
    """ Return the plants overview page """

    plants = Plant.objects.all()
    categories = Category.objects.all()

    if request.GET : 
        if 'category' in request.GET:
            selected_category = request.GET['category']
            plants = Plant.objects.filter(category__name=selected_category)
        if 'query' in request.GET :
            query = request.GET['query']
            queries = Q(common_name__icontains=query) | Q(
                botanical_name__icontains=query) | Q(description__icontains=query)
            plants = Plant.objects.filter(queries)

    context = {
        'plants': plants,
        'categories': categories
    }

    return render(request, 'plants/all_plants.html', context)


def single_plant(request, plant_id):
    """ Show the page for a single plant """

    plant = get_object_or_404(Plant, pk=plant_id)

    context = {
        'plant': plant
    }

    return render(request, 'plants/single_plant.html', context)
