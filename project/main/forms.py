from django.forms import ModelForm
from django import forms
from .models import AlgoModel

ALGO_VALUES = [
    ('1' , 'KL Sum Algorithm' ),
    ('2' , 'LexRank Algorithm' ),
    ('3' , 'LSA Algorithm') 
]

class AlgoSelectorForm(forms.Form) :
    
    algo_name =  forms.CharField(label = "Select an Algorithm to use " , widget = forms.RadioSelect(choices=ALGO_VALUES))
    document_text = forms.CharField(label = "Enter the Text to Summarize " , widget=forms.Textarea(attrs={"rows": 10 , "cols" : 10}))
