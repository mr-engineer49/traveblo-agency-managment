from django import forms
from .models import  Item
from django.forms.widgets import CheckboxInput




INPUT_CLASSES = "py-4 px-8 rounded-2xl border"
INPUT_CLASSES_1 = "w-32 py-4 px-8 rounded-2xl border flex inline-block"
CHECKBOX_CLASSES = "w-32 py-4 px-8 rounded-2xl border flex inline-block bg-green-500"


class PoolBooleanWidget(CheckboxInput):
    input_type = 'checkbox'
    attrs = {'class': INPUT_CLASSES_1}

class FoodBooleanWidget(CheckboxInput):
    input_type = 'checkbox'
    attrs = {'class': CHECKBOX_CLASSES}

class ParkingBooleanWidget(CheckboxInput):
    input_type = 'checkbox'



class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'images', 'destinations', 'pool', 'food', 'parking', 'bedrooms', 'bathrooms', 'persons', 'places', 'restaurants', 'vacations', 'activities', 'trip')
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
            'pool': PoolBooleanWidget(),
            'places': FoodBooleanWidget(),
            'restaurants': FoodBooleanWidget(),
            'vacations': FoodBooleanWidget(),
            'activities': FoodBooleanWidget(),
            'trip': FoodBooleanWidget(),
            'food': FoodBooleanWidget(),
            'parking': ParkingBooleanWidget(),
            'bedrooms': forms.TextInput(attrs={
            'class': INPUT_CLASSES_1
            }),
            'bathrooms': forms.TextInput(attrs={
            'class': INPUT_CLASSES_1
            }),
            'persons': forms.TextInput(attrs={
            'class': INPUT_CLASSES_1
            }),
            'destinations': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'images': forms.FileInput(attrs={})
        }




CHECKBOX_CLASSES = "w-32 py-4 px-8 rounded-2xl border flex inline-block bg-green-500"



class PoolBooleanWidget(CheckboxInput):
    input_type = 'checkbox'
    attrs = {'class': INPUT_CLASSES_1}

class FoodBooleanWidget(CheckboxInput):
    input_type = 'checkbox'
    attrs = {'class': CHECKBOX_CLASSES}


class ParkingBooleanWidget(CheckboxInput):
    input_type = 'checkbox'




class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'images', 'destinations', 'pool', 'food', 'parking', 'bedrooms', 'bathrooms', 'persons', 'places', 'restaurants', 'vacations', 'activities', 'trip')
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
            'pool': PoolBooleanWidget(),
            'places': FoodBooleanWidget(),
            'restaurants': FoodBooleanWidget(),
            'vacations': FoodBooleanWidget(),
            'activities': FoodBooleanWidget(),
            'trip': FoodBooleanWidget(),
            'food': FoodBooleanWidget(),
            'parking': ParkingBooleanWidget(),
            'bedrooms': forms.TextInput(attrs={
            'class': INPUT_CLASSES_1
            }),
            'bathrooms': forms.TextInput(attrs={
            'class': INPUT_CLASSES_1
            }),
            'persons': forms.TextInput(attrs={
            'class': INPUT_CLASSES_1
            }),
            'destinations': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'images': forms.FileInput(attrs={})
        }