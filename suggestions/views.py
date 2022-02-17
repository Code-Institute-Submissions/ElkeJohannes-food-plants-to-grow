from urllib import request
from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import Suggestion
from .forms import SuggestionForm
from django.contrib import messages


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
            suggestion = suggestion_form.save(commit=False)
            suggestion.creator = request.user
            suggestion.save()
            messages.success(request, 'Successfully added suggestion!')
            return redirect(reverse('view_suggestions'))
    else:
        suggestion_form = SuggestionForm()

        context = {
            'suggestion_form': suggestion_form,
        }

        return render(request, 'suggestions/add_suggestion.html', context)


@login_required
def edit_suggestion(request, suggestion_id):
    """
    Load the suggestion in the editor to allow the creator to make changes
    """
    if request.method == "POST":
        suggestion = get_object_or_404(Suggestion, pk=suggestion_id)
        suggestion_form = SuggestionForm(request.POST, instance=suggestion)
        if suggestion_form.is_valid():
            suggestion = suggestion_form.save()
            messages.success(request, 'Suggestion succesfully updated!')
        else:
            messages.warning(request, 'Error while saving, please try again')

        return redirect(reverse('view_suggestions'))
    else:
        suggestion = get_object_or_404(Suggestion, pk=suggestion_id)
        suggestion_form = SuggestionForm(instance=suggestion)
        context = {
            'suggestion_form': suggestion_form,
            'suggestion': suggestion,
        }

        return render(request, 'suggestions/edit_suggestion.html', context)


@login_required
def delete_suggestion(request, suggestion_id):
    """
    Allows the creator to delete the suggestion
    """
    suggestion = get_object_or_404(Suggestion, pk=suggestion_id)
    suggestion.delete()
    messages.warning(request, 'Suggestion succesfully deleted')

    return redirect(reverse('view_suggestions'))


@login_required
def upvote_suggestion(request, suggestion_id):
    """
    Upvotes a suggestion if a user is logged in
    and hasn't voted for this suggestion before
    """
    suggestion = get_object_or_404(Suggestion, pk=suggestion_id)
    user = request.user
    # check if user is in list of upvoters
    upvoters = suggestion.upvoters_as_list()
    if str(user) not in upvoters:
        suggestion.upvoters = str(suggestion.upvoters) + f';{user}'
        suggestion.number_of_upvotes += 1
        messages.success(request, f'Upvoted: {suggestion.common_name}')
        suggestion.save()
    else:
        messages.warning(request, 'You have already voted for this plant')

    return redirect(reverse('view_suggestions'))
