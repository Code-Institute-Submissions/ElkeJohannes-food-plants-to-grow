from django import forms
from .models import Suggestion


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ('common_name', 'botanical_name', 'argument')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'common_name': 'Common Name',
            'botanical_name': 'Botanical Name',
            'argument': 'Why we should add it to the shop..',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
