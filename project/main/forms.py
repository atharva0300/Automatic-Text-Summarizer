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

OPTIONS_VALUES = [
    ('1' , 'Extract text from PDF and summarize'),
    ('2' , 'Summarize input text')
]

class OptionsSelectorForm(forms.Form) : 
    option = forms.CharField(label = "" , widget = forms.RadioSelect(
        choices=OPTIONS_VALUES,
        attrs={
            'style' : 'display : flex; flex-direction : column; justify-content : center; align-items : flex-start;' 
        }
    ))
