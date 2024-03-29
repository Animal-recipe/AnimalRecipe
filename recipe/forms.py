from django import forms
from .models import Recipe_Img,Recipe_Ingredient,Recipe,Recipe_Step
from .widgets import PreviewFileWidget, PreviewFileWidget2

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['animal', 'cooking_time', 'title', 'summary', 'level']

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = Recipe_Img
        fields = ['image']
        widgets = {
            'image': PreviewFileWidget,
        }
        labels = {
            'image': '',
        }

class RecipeIngredientForms(forms.ModelForm):
    class Meta:
        model = Recipe_Ingredient
        fields = ['ingredient','amount']
        widgets = {
            'ingredient': forms.TextInput(
                attrs={
                    'class': 'input_box2',
                    'placeholder': '예시 ) 돼지고기',
                    'maxlength': '50',
                }
            ),
            'amount': forms.TextInput(
                attrs={
                    'class': 'input_box3',
                    'placeholder': '예시 ) 100g',
                    'maxlength': '50',
                }
            ),
        }
        labels = {
            'ingredient': '',
            'amount': '',
        }

class RecipeStepForms(forms.ModelForm):
    class Meta:
        model = Recipe_Step
        fields = ['procedure','image', 'content']
        widgets = {
            'procedure': forms.TextInput(
                attrs={
                        'class': 'nontext',
                         }
            ),
            'image': PreviewFileWidget2,
            'content': forms.Textarea(
                attrs={
                    'class': 'input_box4',
                    'placeholder': '예시) 싱싱한 야채들을 준비하고, 깨끗하게 씻어줍니다.',
                    'maxlength': '500',
                }
            ),
        }
        labels = {
            'procedure': '',
            'image': '',
            'content': '',
        }

RecipeImageFormSet = forms.inlineformset_factory(Recipe, Recipe_Img, form=RecipeImageForm, extra=3)
RecipeIngredientFormSet = forms.inlineformset_factory(Recipe, Recipe_Ingredient, form=RecipeIngredientForms, extra=10)
RecipeStepFormSet = forms.inlineformset_factory(Recipe, Recipe_Step, form=RecipeStepForms, extra=10)
