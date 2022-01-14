from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField
from mptt.models import MPTTModel, TreeForeignKey

from timezone_field import TimeZoneField


class Individual(models.Model):
    MALE = [
        ('1', 'мужской'),
        ('2', 'женский'),
        ('3', 'неизвестно'),
    ]
    TYPE = [
        ('1', 'первичный'),
        ('2', 'повторный'),
        ('3', 'внешний'),
        ('4', 'косвенный'),
    ]
    # last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    # first_name = models.CharField(max_length=255, verbose_name='Имя')
    # middle_name = models.CharField(max_length=255, verbose_name='Отчество')
    #or ↓
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    phone = models.CharField(max_length=155, unique=True, verbose_name='Номер телефон', blank=True, null=True)
    extension_phone = ArrayField(models.CharField(max_length=155, unique=True), blank=True, null=True,  verbose_name='Дополнительные номера')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(verbose_name='Дата изменения', null=True, blank=True)
    status = models.BooleanField(default=False, verbose_name='Статус')
    change_status = models.DateTimeField(verbose_name='Дата изменения статуса', null=True, blank=True)
    email = ArrayField(models.EmailField(), blank=True, null=True, verbose_name='Почта')
    male = models.CharField(max_length=12, choices=MALE,  verbose_name='Пол', blank=True, null=True)
    type = models.CharField(max_length=20, choices=TYPE,  verbose_name='Тип', blank=True, null=True)
    timezone = TimeZoneField(verbose_name='Часовой пояс', blank=True, null=True)
    vk = ArrayField(models.URLField(), blank=True, null=True, verbose_name='В Контакте')
    fb = ArrayField(models.URLField(), blank=True, null=True, verbose_name='Facebook')
    ok = models.URLField(blank=True, null=True, verbose_name='Одноклассники')
    instagram = models.URLField(blank=True, null=True, verbose_name='Instagram')
    telegram = models.URLField(blank=True, null=True, verbose_name='Telegram')
    whatsapp = models.CharField(max_length=255, blank=True, null=True, verbose_name='WhatsApp')
    viber = models.URLField(blank=True, null=True, verbose_name='Viber')

    class Meta:
        verbose_name_plural = 'Физическое лицо (Клиент)'

    def __str__(self):
        return self.full_name


class Department(MPTTModel):
    title = models.CharField(max_length=255, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    individuals = models.ManyToManyField(Individual,  null=True, blank=True, db_index=True, related_name='departments', verbose_name='Физические лица')
    date_add_individual = models.DateField(null=True, blank=True, verbose_name='Дата добавление клиента')

    # в методе save, указываю максимальный уровень вложенности
    def save(self, *args, **kwargs):
        max_indent = 7
        lvl = self.parent.level if self.parent else 0
        if lvl < max_indent:
            super().save(*args, **kwargs)
        else:
            raise ValueError("Максимальная вложенность: 7")

    class Meta:
        verbose_name_plural = 'Департамент'

    def __str__(self):
        return self.title


class Entity(models.Model):
    full_title = models.CharField(max_length=255, verbose_name='Полное название')
    abbreviation = models.CharField(max_length=255, verbose_name='Сокращенное название', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    inn = models.CharField(max_length=20, verbose_name='ИНН', blank=True, null=True)
    kpp = models.CharField(max_length=20, verbose_name='КПП', blank=True, null=True)
    departments = models.ManyToManyField(Department, blank=True, null=True, verbose_name='Департаменты')

    class Meta:
        verbose_name_plural = 'Юридическое лицо'

    def __str__(self):
        return self.full_title
