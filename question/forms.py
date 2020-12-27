from django import forms
from .models import Question, Answer
from django.utils.translation import ugettext_lazy as _ 

class QuestionForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        max_length=100,
        widget = forms.TextInput(
            attrs={
                'class' : 'questionTitle',
                'placeholder' : _('예시 ) 너무 쉽고 맛있는 황태국 (15자 이내)'),
                'required' : 'True',
            } 
        )
    )
    content = forms.CharField(
        label='',
        max_length=2000,
        widget = forms.Textarea(
            attrs={
                'class' : 'questionContent',
                'placeholder' : _('예시 ) 개인정보(실명 및 연락처, 구체적인 주소 등)가 포함되지 않아야 합니다. 질문을 제외한 상업적 게시글 혹은 홍보성 게시글, 분양 등의 게시글은 무통보 삭제되며 계정 정지 등의 조치가 취해질 수 있습니다.'),
                'required' : 'True',
                'rows' : 15,
            } 
        )
    )
    class Meta:
        model= Question
        fields = ('title', 'content')

class AnswerForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        max_length=2000,
        widget = forms.Textarea(
            attrs={
                'class' : 'answerContent',
                'placeholder' : _('예시 ) 개인정보(실명 및 연락처, 구체적인 주소 등)가 포함되지 않아야 합니다. 답변을 제외한 상업적 게시글 혹은 홍보성 게시글, 분양 등의 게시글은 무통보 삭제되며 계정 정지 등의 조치가 취해질 수 있습니다.'),
                'required' : 'True',
                'rows' : 15,
            } 
        )
    )
    class Meta:
        model= Answer
        fields = ('content',)
