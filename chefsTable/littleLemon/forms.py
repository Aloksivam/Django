from django import forms
from .models import Demoformer
# fvt_dish=[
#         ('italian','Italian'),
#         ('greek','Greek'),
#         ('turkish','Turkish'),
#         ]
# class Demoform(forms.Form):
#     name=forms.CharField()
#     name=forms.CharField(widget=forms.Textarea)
#     name=forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
#     email=forms.EmailField(label="enter your email")
#     reserv_date=forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    # fvtdish=forms.ChoiceField(choices=fvt_dish)
#     fvtdish=forms.ChoiceField(widget=forms.RadioSelect ,choices=fvt_dish)
    #for choices
   
class Demoform(forms.ModelForm):
    class Meta:
        model=Demoformer
        fields='__all__'
