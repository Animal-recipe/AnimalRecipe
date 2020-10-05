from django import forms
from .models import Review_Img,Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'cooking_time', 'title', 'summary', 'count', 'level']

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = Review_Img
        fields = ['image']
        widgets = {
            'image': forms.FileInput(
                attrs={
                            'class': 'recipe_img',
                        }
            )
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
                    'class': 'ingredient_box',
                    'placeholder': '재료',
                }
            ),
            'amount': forms.TextInput(
                attrs={
                    'class': 'amount_box',
                    'placeholder': '양',
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
        fields = ['image', 'content']
        widgets = {
            'image': forms.FileInput(
                attrs={
                            'class': 'step_img',
                        }
            ),
            'content': forms.TextInput(
                attrs={
                    'class': 'content_box',
                    'placeholder': '조리 방법',
                }
            ),
        }
        labels = {
            'image': '',
            'content': '',
        }

RecipeImageFormSet = forms.inlineformset_factory(Recipe, Recipe_Img, form=RecipeImageForm, extra=3)
RecipeIngredientFormSet = forms.inlineformset_factory(Recipe, Recipe_Ingredient, form=RecipeIngredientForms, extra=5)
RecipeStepFormSet = forms.inlineformset_factory(Recipe, Recipe_Step, form=RecipeStepForms, extra=10)