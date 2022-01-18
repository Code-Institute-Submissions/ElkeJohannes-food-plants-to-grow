from django.shortcuts import render, reverse, redirect
from .forms import ContactForm


def contact_form(request):
    """
    Send the form if request = POST
    Add a contact form if request = GET
    """
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # Send an email
            return redirect(reverse('home'))
    else:
        contact_form = ContactForm()

        context = {
            'contact_form': contact_form,
        }
        
        return render(request, 'contact/contact.html', context)
