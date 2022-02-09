from django.shortcuts import render, redirect, reverse
from .forms import UserAccountForm
from .models import UserAccount


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
            user_account_form.save()
        return redirect(reverse('profile'))
    else:
        user_account_form = UserAccountForm(instance=request.user)
        context = {
            'user_account_form': user_account_form
        }

        return render(request, 'accounts/profile.html', context)
