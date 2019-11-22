from django.db import forms

# class BookForm(forms.Modelform):
#     class Meta:
#         model=Book
#         fields=['name','preface']

class BookForm(forms.Form):
    name = forms.CharField(max_length=20)
    preface = forms.CharField(max_length=100)