from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib.auth.decorators import login_required

from .models import Suggestion
from .forms import SuggestionForm


def view_suggestions(request):
    """
    View all submitted suggestions
    """
    suggestions = Suggestion.objects.all().order_by('-number_of_upvotes')

    context = {
        'suggestions': suggestions,
    }

    return render(request, 'suggestions/view_suggestions.html', context)

@login_required
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

@login_required
def upvote_suggestion(request, suggestion_id):
    """
    Upvotes a suggestion if a user is logged in
    and hasn't voted for this suggestion before
    """
    suggestion = get_object_or_404(Suggestion, pk=suggestion_id)
    user = request.user
    # check if user is in list of upvoters
    if not user in suggestion.upvoters.all() :
        print("user is not in the list")
        print(user)
        suggestion.upvoters.add(user)
        suggestion.number_of_upvotes += 1
        suggestion.save()
    
    return redirect(reverse('view_suggestions'))
