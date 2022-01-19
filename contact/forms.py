from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(
                                attrs={'placeholder': 'John Doe *'}),
                                max_length=100, label=False)
    email = forms.CharField(widget=forms.EmailInput(
                            attrs={'placeholder': 'you@youremail.com *'}),
                            max_length=100, label=False)
    phone_number = forms.CharField(widget=forms.NumberInput(
                                   attrs={'placeholder': '+31612345678'}),
                                   required=False, label=False)
    question = forms.CharField(widget=forms.Textarea(
                               attrs={'placeholder': 'Question: why is this the best site ever? *'}),
                               label=False)
