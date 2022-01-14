from django.contrib import admin
from django.db.models import Count
from django.utils import timezone

from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from account.models import *


@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fieldsets = (
        ('Oсновная информация', {
        'fields': ('full_name', 'phone', 'extension_phone', 'status',
                   'change_status', 'email', 'male', 'type', 'timezone', 'updated_at')
    }),
        ('Социальные сети', {
        'fields': ('vk', 'fb', 'ok', 'instagram', 'telegram', 'whatsapp', 'viber')
    }),
    )
    list_display = ['id', 'full_name', 'timezone', 'created_at', 'updated_at', 'status', 'change_status']

    # указываю в save_model(методе) дату изменения статуса и изменения данных
    def save_model(self, request, obj, form, change):
        if 'status' in form.changed_data:
            obj.change_status = timezone.now()
        else:
            obj.updated_at = timezone.now()
        obj.save()



@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_title', 'created_at', 'updated_at']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'parent', 'date_add_individual', 'number_of_clients']

    # указываю в save_model(методе) дату добавления клиента в департамент
    def save_model(self, request, obj, form, change):
        if 'individuals' in form.changed_data:
            obj.date_add_individual = timezone.now()
        obj.save()

    # в списке департаментов вывожу кол-во физ-лица(клиетов)
    def number_of_clients(self, obj):
        return obj.number_of_clients

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            number_of_clients=Count("individuals", distinct=True),
        )
        return queryset
