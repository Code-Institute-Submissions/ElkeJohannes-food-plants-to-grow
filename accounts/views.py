from django.shortcuts import render

def profile(request):
    """ Return the users profile page """

    return render(request, 'accounts/profile.html')
