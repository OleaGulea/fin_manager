from django import forms
from crispy_forms.helper import FormHelper

from fin_manager.categories.models import Entry, Category


class EntryForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    amount = forms.FloatField()

    class Meta:
        model = Entry
        fields = ['category', 'date', 'amount']
