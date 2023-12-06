from django import forms

class OptionCreationForm(forms.Form):
    photo = forms.ImageField()
    category = forms.CharField()
    description = forms.CharField()
    email = forms.EmailField()


