from django.db import models
from django.urls import reverse
from django.conf import settings
from account.models import User

class Question(models.Model):
    # 유저
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question_user')
    # 제목
    title = models.TextField(max_length=100, default='')
    # 내용
    content = models.TextField(max_length=2000, default='')
    # 작성 시간
    created = models.DateTimeField(auto_now_add=True)
    # 수정 시간
    updated = models.DateTimeField(auto_now=True)
    # 활성화 여부
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('question:detail', args=[self, id])


class Answer(models.Model):
    # 유저
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_user')
    #question
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answer")
    # 내용
    content = models.TextField(max_length=2000, default='')
    # 작성 시간
    created = models.DateTimeField(auto_now_add=True)
    # 수정 시간
    updated = models.DateTimeField(auto_now=True)
    # 공감
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_answer', blank=True)
    # 채택
    accept = models.BooleanField(default=False)
    # 활성화 여부
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question.title

    class Meta:
        ordering = ['-created', '-accept']
