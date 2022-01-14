# Generated by Django 3.2.6 on 2022-01-14 10:17

from django.db import migrations, models
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_individual_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Сокращенное название'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='inn',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='kpp',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='КПП'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='male',
            field=models.CharField(blank=True, choices=[('1', 'мужской'), ('2', 'женский'), ('3', 'неизвестно')], max_length=12, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='phone',
            field=models.CharField(blank=True, max_length=155, null=True, unique=True, verbose_name='Номер телефон'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(blank=True, null=True, verbose_name='Часовой пояс'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='type',
            field=models.CharField(blank=True, choices=[('1', 'первичный'), ('2', 'повторный'), ('3', 'внешний'), ('4', 'косвенный')], max_length=20, null=True, verbose_name='Тип'),
        ),
    ]
