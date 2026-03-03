from django import forms
from .models import shoe_todo

class ShoeTodoForm(forms.ModelForm):
    class Meta:
        model = shoe_todo
        fields = ['message', 'status']

class InputForm(forms.Form):
    my_input = forms.CharField(widget=forms.SubmitInput(attrs={'class': 'button'}))