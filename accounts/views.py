from django.shortcuts import render, redirect, reverse
from .forms import UserAccountForm
from .models import UserAccount
from django.contrib import messages


def profile(request):
    """
    Return the users profile page if GET
    Else, save the form as a userprofile
    """

    if request.method == "POST":
        current_user = request.user
        user_profile = UserAccount.objects.get(pk=current_user.id)
        user_account_form = UserAccountForm(request.POST,
                                            instance=user_profile)
        if user_account_form.is_valid():
            messages.success(request, 'Profile succesfully updated!')
            user_account_form.save()
        else:
            messages.warning(request, 'Profile failed to save, please try again.')
        return redirect(reverse('profile'))
    else:
        user_account_form = UserAccountForm(instance=request.user)
        context = {
            'user_account_form': user_account_form
        }

        return render(request, 'accounts/profile.html', context)
