from django import forms
from .models import Concert

class ConcertForm(forms.ModelForm):
    class Meta:
         model = Concert
         fields = ('venue', 'city','country','concert_date',)
