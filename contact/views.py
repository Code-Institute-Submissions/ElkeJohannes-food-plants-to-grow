from django.shortcuts import render, reverse, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def contact_form(request):
    """
    Send an email if request = POST
    Add a contact form if request = GET
    """
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # Send an email
            sender = contact_form.cleaned_data['email']
            question = contact_form.cleaned_data['question']
            mail_body = f'From: {sender} \nQuestion: {question}'
            send_mail(
                "New message from Contactform",
                mail_body,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False
            )
            return redirect(reverse('home'))
    else:
        contact_form = ContactForm()

        context = {
            'contact_form': contact_form,
        }

        return render(request, 'contact/contact.html', context)
