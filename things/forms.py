"""Forms of the project."""

# Create your forms here.

from django import forms

class ThingForm(forms.Form):
    """Form for adding things to the database."""
    name = forms.CharField(max_length=35, required=True)
    description = forms.Textarea(max_length=120, required=False)
    quantity = forms.NumberInput(min_value=0, max_value=50, required=True)
    