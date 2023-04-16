from django.forms import ModelForm
from django import forms
from .models import AlgoModel

ALGO_VALUES = [
    ('1' , 'KL Sum Algorithm' ),
    ('2' , 'LexRank Algorithm' ),
    ('3' , 'LSA Algorithm') 
]

class AlgoSelectorForm(forms.Form) :
    
    algo_name =  forms.CharField(label = "Select an Algorithm to use " , widget = forms.RadioSelect(
        choices=ALGO_VALUES,
        attrs = {
            'class' : 'form-check-inline'
        }))
    document_text = forms.CharField(label = "Enter the Text to Summarize " , widget=forms.Textarea(
        attrs={
            'class' : 'form-control',
            'style' : 'height : 1000px;'
        }
        ))


class ChangeAlgoForm(forms.Form) : 
    algo_name =  forms.CharField(label = "Change Algorithm" , widget = forms.RadioSelect(
        attrs = {
            'class' : 'form-check-inline'
        },
        choices=ALGO_VALUES
        ))