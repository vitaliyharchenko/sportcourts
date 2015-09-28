# coding=utf-8
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core.mail import send_mail
from django.utils import timezone
from utils.validators import validate_height, validate_weight
from utils.witgets import JasnyImageModelField, MyPhoneField
from courts.models import City
import datetime
from utils.formatters import age_format


class AbstractUserManager(BaseUserManager):
    def _create_user(self, email, password, is_superuser, is_staff, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('Email должен быть задан')
        email = self.normalize_email(email)

        is_active = extra_fields.pop("is_active", True)
        is_responsible = extra_fields.pop("is_responsible", False)
        is_admin = extra_fields.pop("is_admin", False)
        first_name = extra_fields.pop("first_name", '')
        last_name = extra_fields.pop("last_name", '')

        user = self.model(
            email=self.normalize_email(email),
            is_active=is_active,
            is_responsible=is_responsible,
            is_staff=is_staff,
            is_admin=is_admin,
            is_superuser=is_superuser,
            first_name=first_name,
            last_name=last_name,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        Activation.objects.create(email=email, status=Activation.REGISTERED, token='manual adding')

        return user

    # create regular user
    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email', max_length=255, unique=True, db_index=True)

    is_active = models.BooleanField('Активность', default=True,
                                    help_text="Сделайте неактивным вместо удаления аккаунта")
    is_referee = models.BooleanField('Судья', default=False,
                                     help_text="Может судить игры")
    is_coach = models.BooleanField('Тренер', default=False,
                                   help_text="Может вести тренировки")
    is_responsible = models.BooleanField('Ответственный', default=False,
                                         help_text="Заполняет отчеты, редактирует игры")
    is_organizer = models.BooleanField('Организатор', default=False,
                                       help_text="Создает игры, площадки, назначает ответственных")
    is_admin = models.BooleanField('Админ', default=False,
                                   help_text="Назначает организаторов, работает с зарплатами и базами данных")
    is_staff = models.BooleanField('Статус сотрудника', default=False,
                                   help_text="Определяет , может ли пользователь войти в админку")

    banned = models.BooleanField('Бан', default=False,
                                   help_text="Ставит бан пользователю")
    # TODO: Jasny image field
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True, verbose_name='Аватар')

    date_joined = models.DateTimeField('Дата регистрации', default=timezone.now)
    bdate = models.DateField('Дата рождения', auto_now_add=False, blank=True, null=True)

    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)

    vkuserid = models.IntegerField(unique=True, null=True, blank=True)
    sex = models.CharField(max_length=1, choices=(('m', 'муж.'), ('f', 'жен.')), verbose_name='Пол')

    phone = MyPhoneField(verbose_name=u'Телефон', unique=True, blank=True)
    # TODO: create my own phone field
    # https://github.com/daviddrysdale/python-phonenumbers

    ampluas = models.ManyToManyField('events.Amplua', verbose_name=u'Амплуа', blank=True)
    weight = models.PositiveSmallIntegerField(default=0, verbose_name='Вес', validators=[validate_weight])
    height = models.PositiveSmallIntegerField(default=0, verbose_name='Рост', validators=[validate_height])
    city = models.ForeignKey(City, null=True, blank=True, verbose_name='Город')
    # settings = models.OneToOneField('users.UserSettings', verbose_name='Настройки')
    # TODO: add settings model

    objects = AbstractUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    REGISTRATION_FIELDS = ['avatar'] + REQUIRED_FIELDS + ['sex'] + ['vkuserid'] + ['bdate'] + ['phone'] + [USERNAME_FIELD] + ['password']

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'
        abstract = True

    def get_full_name(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.email

    def get_beautiful_phone(self):
        phone = self.phone.__str__()
        return phone[:2] + ' (' + phone[2:5] + ') ' + phone[5:8] + '-' + phone[8:10] + '-' + phone[10:12]

    @property
    def age(self):
        today = datetime.date.today()
        return today.year - self.bdate.year - ((today.month, today.day) < (self.bdate.month, self.bdate.day))

    def beautiful_age(self):
        return age_format(self.age)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.last_name)


class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        app_label = 'customuser'

    def get_absolute_url(self):
        return "/users/%i" % self.id


class Activation(models.Model):
    EMAIL_SENT = 0
    EMAIL_VERIFIED = 1
    REGISTERED = 2

    email = models.EmailField(primary_key=True, unique=True, verbose_name='Email')
    status = models.IntegerField(default=EMAIL_SENT, verbose_name='Статус',
                                 choices=((EMAIL_SENT, 'Сообщение отправлено'),
                                          (EMAIL_VERIFIED, 'Подтверждено'),
                                          (REGISTERED, 'Зарегестрирован')))
    token = models.CharField(max_length=100, verbose_name='Ключ активации', unique=True)
    datetime = models.DateTimeField('Дата активации', auto_now=True)

    class Meta:
        ordering = ['-datetime']
        app_label = 'customuser'
        verbose_name = 'подтверждение почты'
        verbose_name_plural = 'Подтверждения почты'

    def __unicode__(self):
        return self.email