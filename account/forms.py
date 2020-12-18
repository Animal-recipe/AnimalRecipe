from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.files.images import get_image_dimensions
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, PET_KINDS


class UserCreationForm(forms.ModelForm):

    email = forms.EmailField(
        label=_('이메일'),
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('이메일 주소'),
                'required': 'True',
            }
        )
    )
    nickname = forms.CharField(
        label=_('닉네임'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('닉네임'),
                'required': 'True',
            }
        )
    )

    profile = forms.ImageField(label='프로필 사진')
    password1 = forms.CharField(label='비밀번호', 
        widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('비밀번호'),
                    'required': 'True',
                }
        )
    )
    password2 = forms.CharField(
        label='비밀번호 확인', 
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('비밀번호 확인'),
                'required': 'True',
            }
        )
    )

    petname = forms.CharField(
        label=_('반려동물 이름'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('반려동물 이름'),
                'required': 'True',
            }
        )
    )

    petkind = forms.CharField(
        label='반려동물 종류',
        max_length=4,
        widget=forms.Select(choices=PET_KINDS),
    )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'nickname', 'petname', 'petkind', 'profile')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('password', 'nickname', 'petname', 'petkind', 'profile')
    
    def clean_password(self):
        return self.initial["password"]
