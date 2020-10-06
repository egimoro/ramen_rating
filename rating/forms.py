from .models import Ramen
from django import forms

class RamenForm(forms.ModelForm):



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stars'].widget.attrs.update({'type':'number', 'min':0})
        self.fields['dateReview'].widget = forms.widgets.DateTimeInput(attrs=({'type': 'datetime-local'}))  
        self.fields['formram'] = forms.CharField(widget=forms.HiddenInput(),
         required=False, label='')
    
    

       
    class Meta:
        model = Ramen
        fields = ['brand', 'variety', 'style', 'country', 'stars', 'dateReview', 'topTen']
        
        