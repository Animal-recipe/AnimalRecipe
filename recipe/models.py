from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta
from django.utils import timezone
from django.urls import reverse
from account.models import User

# Create your models here.

class Recipe(models.Model):
    # 유저
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_user')
    # 반려동물
    animal = models.CharField(max_length=10, default='')
    # 조리시간
    cooking_time = models.CharField(max_length=50, default='')
    # 제목
    title = models.TextField(max_length=100, default='')
    # 요약설명
    summary = models.TextField(max_length=500, default='')
    # 작성 시간
    created = models.DateTimeField(auto_now_add=True)
    # 수정 시간
    updated = models.DateTimeField(auto_now=True)
    # 공감
    like = models.ManyToManyField(User, related_name='like_recipe', blank=True)
    # 스크랩 수
    bookmark = models.ManyToManyField(User, related_name='save_recipe', blank=True)
    # 조회수
    hits = models.PositiveIntegerField(default=0)
    # 난이도
    level = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('recipe:detail', args=[self, id])

    def title_limit(self):
        return self.title[:20]

    def created_string(self):
        time = timezone.now() - self.updated

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = timezone.now().date() - self.updated.date()
            return str(time.days) + '일 전'
        else:
            return self.updated

    def update_counter(self):
        self.hits = self.hits + 1
        self.save()

class Recipe_Img(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_img")
    image = models.ImageField(upload_to='recipe_img/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.recipe.title

class Recipe_Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_ingredient")
    # 재료
    ingredient = models.CharField(max_length=50, null=True)
    # 양
    amount = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.recipe.title

class Recipe_Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_step")
    # 순서
    procedure = models.TextField(max_length=50, default='')
    # 이미지
    image = models.ImageField(upload_to='recipe_step/%Y/%m/%d', blank=True)
    # 내용
    content = models.TextField(max_length=500, default='')

    def __str__(self):
        return self.recipe.title
