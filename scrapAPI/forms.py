from django import forms

class TwForm(forms.Form):
    username = forms.CharField(label='Twitter Username', max_length=200)