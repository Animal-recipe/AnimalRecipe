from django import forms
from .models import Message
from django.forms import ModelChoiceField
from account.models import User

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

        widgets = {
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '쪽지를 작성해주세요.',
                }
            ),
        }

class RemessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

        widgets = {
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '쪽지를 작성해주세요.',
                }
            ),
        }