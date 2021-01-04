from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.files.images import get_image_dimensions
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, PET_KINDS
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

class UserCreationForm(forms.ModelForm):

    email = forms.EmailField(
        label='',
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                'class': 'registerInput',
                'placeholder': _('이메일'),
                'required': 'True',
            }
        )
    )
    nickname = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'registerInput',
                'placeholder': _('닉네임(중복불가)'),
                'required': 'True',
            }
        )
    )
    profile = forms.ImageField(label='', required=False)
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
                attrs={
                    'class': 'registerInput',
                    'placeholder': _('비밀번호(8자리 이상)'),
                    'required': 'True',
                }
        )
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'registerInput',
                'placeholder': _('비밀번호 확인'),
                'required': 'True',
            }
        )
    )
    petname = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'registerInput',
                'placeholder': _('반려동물 이름'),
                'required': 'True',
            }
        )
    )
    petkind = forms.CharField(
        label='',
        widget= forms.Select(
            choices=PET_KINDS,
            attrs={
                'placeholder': _('반려동물을 선택해주세요'),
                'class': 'registerInput',
            }
        )
    )

    class Meta:
        model = User
        fields = ('profile', 'email',  'nickname', 'password1', 'password2', 'petkind', 'petname')

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise forms.ValidationError("비밀번호는 8자 이상이어야 합니다.")
        return password1
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
        return password2
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('이메일 중복을 확인해 주세요.')
        return email
    def clean_nickname(self):
        nickname = self.cleaned_data.get("nickname")
        if User.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError('닉네임 중복으로 사용하실 수 없습니다.')
        return nickname
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.passwordLength = len(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    email = forms.EmailField(
        label='',
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                'class': 'registerInput',
                'placeholder': _('이메일'),
                'required': 'True',
            }
        )
    )
    nickname = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'registerInput',
                'placeholder': _('닉네임(중복불가)'),
                'required': 'True',
            }
        )
    )
    profile = forms.ImageField(label='', required=False)
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
                attrs={
                    'class': 'registerInput',
                    'placeholder': _('비밀번호(8자리 이상)'),
                    'required': 'True',
                }
        )
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'registerInput',
                'placeholder': _('비밀번호 확인'),
                'required': 'True',
            }
        )
    )
    petname = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'registerInput',
                'placeholder': _('반려동물 이름'),
                'required': 'True',
            }
        )
    )
    petkind = forms.CharField(
        label='',
        widget= forms.Select(
            choices=PET_KINDS,
            attrs={
                'placeholder': _('반려동물을 선택해주세요'),
                'class': 'registerInput',
            }
        )
    )
    class Meta:
        model = get_user_model()
        fields = ('email', 'profile', 'nickname', 'password1', 'password2', 'petkind', 'petname')

    def clean_nickname(self):
        nickname = self.cleaned_data.get("nickname")
        email=self.cleaned_data.get("email")
        if User.objects.filter(nickname=nickname).exclude(email=email).exists():
            raise forms.ValidationError('닉네임 중복으로 사용하실 수 없습니다.')
        return nickname
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise forms.ValidationError("비밀번호는 8자 이상이어야 합니다.")
        return password1
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
        return password2
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.passwordLength = len(self.cleaned_data["password1"])
        if commit:
            user.save()
            print('change form save')
        return user

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs = {
                'class' : 'loginInput'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {
                'class' : 'loginInput'
            }
        )
    )
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if email and password :
            try:
                user = User.objects.get(email = email)
            except User.DoesNotExist:
                self.add_error('email', "존재하지 않는 이메일입니다.")
            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')
        return cleaned_data
