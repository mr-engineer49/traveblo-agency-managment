from django import forms
from .models import  Item

INPUT_CLASSES = "w-full py-4 px-6 rounded-2xl border"

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'images')
        widgets = {
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'description': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'images': forms.FileInput(attrs={
            'class': INPUT_CLASSES
            })
        }



class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'images')
        widgets = {
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'description': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'images': forms.FileInput(attrs={
            'class': INPUT_CLASSES
            })
        }