from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

from dateutil.relativedelta import relativedelta

# Create your models here.
from MySite.settings import USER_MIN_AGE


def birth_date_validator(value):
    age_diff = relativedelta(date.today(), value).years
    if age_diff < USER_MIN_AGE:
        raise ValidationError(f"Невозможно зарегистрировать пользователя моложе {USER_MIN_AGE} лет!")
    return value


class UserRoles:
    USER = "user"
    ADMIN = "admin"
    MODERATOR = "moderator"
    choices = (
        (USER, "Пользователь"),
        (ADMIN, "Администратор"),
        (MODERATOR, "Модератор")
    )


class User(AbstractUser):

    first_name = models.CharField(verbose_name="Имя", max_length=100)
    last_name = models.CharField(verbose_name="Фамилия", max_length=100)
    username = models.CharField(verbose_name="Никнейм", max_length=50, unique=True)
    role = models.CharField(verbose_name="Группа", choices=UserRoles.choices, default="member", max_length=16)
    age = models.PositiveIntegerField(verbose_name="Возраст", null=True)
    birth_date = models.DateField(verbose_name="Дата рождения", max_length=10, validators=[birth_date_validator])
    email = models.EmailField(verbose_name="Электронная почта", max_length=50, unique=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

