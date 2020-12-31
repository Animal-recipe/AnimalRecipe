from django import forms
from .models import Review_Img,Review
from recipe.widgets import PreviewFileWidget

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'star', 'content']

class ReviewImageForm(forms.ModelForm):
    class Meta:
        model = Review_Img
        fields = ['image']
        widgets = {
            'image': PreviewFileWidget,
        }
        labels = {
            'image': '',
        }

ReviewImageFormSet = forms.inlineformset_factory(Review, Review_Img, form=ReviewImageForm, extra=3)
