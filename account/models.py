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
]

# 카테고리 연결하고 회원가입, 로그인, 로그아웃, 마이페이지....
class UserManager(BaseUserManager):
    def create_user(self, email, nickname, petname, petkind, avatar, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nickname = nickname,
            petname=petname,
            petkind=petkind,
            avatar=avatar,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, petname, petkind, avatar, password):
        user = self.create_user(
            email,
            password=password,
            nickname = nickname,
            petname=petname,
            petkind=petkind,
            avatar=avatar,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(
        verbose_name='nickname',
        max_length=20,
        null=False,
        unique=True,
    )
    petname = models.CharField(
        verbose_name='petname',
        max_length=20,
        null=True,
    )

    petkind = models.CharField(max_length=4, choices=PET_KINDS, default='DOG')

    avatar = models.ImageField(
        verbose_name="avatar",
        upload_to='avatars/',
        default='avatars/2.PNG',
        blank=True, null=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname, petname, petkind, avatar']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    def is_staff(self):
        return self.is_admin
