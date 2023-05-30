from django import forms

class PostForm(forms.Form):
    titolo = forms.CharField()
    descrizione = forms.CharField(widget=forms.Textarea())
    