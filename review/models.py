from django.db import models
from django.conf import settings
from recipe.models import Recipe
from django.urls import reverse
from datetime import timedelta
from django.utils import timezone
from account.models import User

class Review(models.Model):
    # 작성자
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_user')
    # 레시피
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_review")
    # 제목
    title = models.TextField(max_length=180, default='')
    # 별점
    star = models.CharField(max_length=50,  default='')
    # 내용
    content = models.TextField(max_length=180, default='')
    # 생성일
    created = models.DateTimeField(auto_now_add=True)
    # 수정일
    updated = models.DateTimeField(auto_now=True)
    # 공감
    # like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_recipe', blank=True)

    def __str__(self):
        return self.recipe.title

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('review:detail', args=[self, id])

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

class Review_Img(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="review_img")
    image = models.ImageField(upload_to='review_img/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.review.recipe.title
