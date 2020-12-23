from django.db import models
from account.models import User

# Create your models here.
class AD(models.Model):
    # 이름
    name = models.CharField(max_length=50, default='')
    # 연락처
    phone = models.CharField(max_length=50, default='')
    # 문의내용
    content = models.TextField(max_length=180, default='')

    def __str__(self):
        return self.name


class Service_center(models.Model):
    # 이름
    name = models.CharField(max_length=50, default='')
    # 연락처
    phone = models.CharField(max_length=50, default='')
    # 문의내용
    content = models.TextField(max_length=180, default='')

    def __str__(self):
        return self.name

class Report_problem(models.Model):
    # 신고하는 사람
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_author', default='')
    # 신고 대상
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_name', default='')
    # 신고사유
    reason = models.CharField(max_length=100, default='')
    # 기타 신고사유
    other_reason = models.TextField(max_length=180, default='')

    def __str__(self):
        return self.name.email

