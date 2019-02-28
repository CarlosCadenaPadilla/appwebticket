from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['title','description','link']
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo del evento'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'link' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Link del evento'}),

        }
        labels = {
           # 'title':'', 'description':'', 'link':'',
        }