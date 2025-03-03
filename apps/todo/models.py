from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    # username и email имеются внутри AbstractUser
    phone_number = models.CharField(
        max_length=13,
        verbose_name="Номер телефона",
        help_text='Номер телефона должен быть в формате +996XXXXXXXXX'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    age = models.PositiveIntegerField(
        verbose_name='Возраст',
        null=True, blank=True,
        help_text='Тут нужно писать свой возраст'
    )
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"  

class Todo(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        unique=True
    )

    description = models.TextField(
        verbose_name="Описание"
    )

    is_completed = models.BooleanField(
        verbose_name="Завершено",
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    
    image = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True,
        verbose_name="Изображение задания"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

