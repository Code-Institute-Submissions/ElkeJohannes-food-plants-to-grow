from multiprocessing import context
from django.shortcuts import render

import suggestions
from .models import Suggestion


def view_suggestions(request):
    """
    View all submitted suggestions
    """
    suggestions = Suggestion.objects.all()

    context = {
        'suggestions': suggestions,
    }

    return render(request, 'suggestions/view_suggestions.html', context)
