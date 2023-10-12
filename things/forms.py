"""Forms of the project."""

# Create your forms here.

from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class ThingForm(forms.Form):
    """Form for adding things to the database."""
    name = forms.CharField(label="name", max_length=35)
    description = forms.CharField(label="description", max_length=120, widget=forms.Textarea)
    quantity = forms.IntegerField(label="quantity", validators=[MinValueValidator(0),MaxValueValidator(50)], widget=forms.NumberInput(attrs={'type':'range', 'step':1, 'value':0, 'onchange':'updateTextInput(this.value);'}))
    