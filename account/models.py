from django.db import models
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

PET_KINDS = [
    ('DOG', '개'),
    ('CAT', '고양이'),
    ('RAB', '토끼'),
    ('BIRD', '새'),
    ('FISH', '물고기'),
    ('HAM', '햄스터'),
    ('ETC', '기타'),
    ('NONE', '없음'),
]

# 카테고리 연결하고 회원가입, 로그인, 로그아웃, 마이페이지....
class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', False)
        extra_fields.setdefault('is_active', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email,  password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')      

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(
        verbose_name='nickname',
        default='nickname',
        max_length=20,
        null=False,
        blank=False,
        unique=True,
    )
    petname = models.CharField(
        verbose_name='petname',
        default='petname',
        max_length=20,
        null=True,
        blank=True,
    )
    petkind = models.CharField(max_length=4, choices=PET_KINDS,blank=False, null=False)
    profile = models.ImageField(
        verbose_name="profile",
        upload_to='profiles/',
        default='profiles/defaultProfile.png',
        blank=True, null=True,
    )
    passwordLength = models.SmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin
