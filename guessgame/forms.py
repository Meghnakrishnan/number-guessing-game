from django import forms

class InputtingForm(forms.Form):
    guess = forms.IntegerField(
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Guess a number between 1-10',
            'min': '1',
            'max': '10',
        })
    )