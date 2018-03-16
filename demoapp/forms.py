from django import forms
from .models import Cars, Brands, Colors
import re


class CarSearchForm(forms.Form):
    brand = forms.CharField(min_length=3, max_length=10)
    model = forms.CharField(required=False)
    year = forms.CharField()

    def clean_year(self):
        year = self.cleaned_data['year']
        if not re.match(r'^\d{4}$', year):
            raise forms.ValidationError('Invalid year format.')
        return year


class CarsForm(forms.Form):
    name = forms.CharField()
    year = forms.RegexField(r'^\d{4}$')
    brand = forms.ModelChoiceField(queryset=Brands.objects.all())
    color = forms.ModelMultipleChoiceField(queryset=Colors.objects.all())

