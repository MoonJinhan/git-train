from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        #meta는 
        model = Board
        fields = ['title','content']