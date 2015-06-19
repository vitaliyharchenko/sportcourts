# coding=utf-8
from django.core.exceptions import ValidationError


def validate_password(value):
    if len(value) < 4:
        raise ValidationError('Пароль слишком уж короткий!')
    if not all(map(lambda x: 97 <= ord(x) <= 122 or x.isdigit(), value.lower())):
        raise ValidationError('Только латинские буквы или цифры.')