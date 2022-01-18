from multiprocessing import context
from django.shortcuts import render, reverse, redirect

import suggestions
from .models import Suggestion
from .forms import SuggestionForm


def view_suggestions(request):
    """
    View all submitted suggestions
    """
    suggestions = Suggestion.objects.all()

    context = {
        'suggestions': suggestions,
    }

    return render(request, 'suggestions/view_suggestions.html', context)


def add_suggestion(request):
    """
    Add a suggestion form if request = GET
    Submits the form if request = POST
    """
    if request.method == "POST":
        suggestion_form = SuggestionForm(request.POST)
        if suggestion_form.is_valid():
            suggestion_form.save()
            return redirect(reverse('view_suggestions'))
    else:
        suggestion_form = SuggestionForm()

        context = {
            'suggestion_form': suggestion_form,
        }
        
        return render(request, 'suggestions/add_suggestion.html', context)
