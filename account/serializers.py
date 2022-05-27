from rest_framework import serializers
from timezone_field.rest_framework import TimeZoneSerializerField

from account.models import Entity, Department, Individual


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['departments'] = DepartmentSerializer(instance.departments, many=True).data
        return representation


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        # fields = ('id', 'parent', 'title', 'date_add_individual', 'individuals')
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['individuals'] = IndividualSerializer(instance.individuals, many=True).data
        # representation['parent'] = instance.parent.__str__() if instance.parent else None
        representation['children'] = DepartmentSerializerInline(instance.children.all(), many=True).data
        return representation


class DepartmentSerializerInline(serializers.ModelSerializer):
    class Meta:
        model = Department
        # fields = ('id', 'parent', 'title', 'date_add_individual', 'individuals')
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['individuals'] = IndividualSerializer(instance.individuals, many=True).data
        representation['parent'] = instance.parent.__str__() if instance.parent else None
        # representation['children'] = DepartmentSerializerInline1(instance.children.all(), many=True).data
        # representation['children'] = instance.children.__str__()
        return representation


# class DepartmentSerializerInline1(serializers.ModelSerializer):
#     class Meta:
#         model = Department
#         # fields = ('id', 'parent', 'title', 'date_add_individual', 'individuals')
#         fields = '__all__'
#
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['individuals'] = IndividualSerializer(instance.individuals, many=True).data
#         representation['parent'] = instance.parent.__str__() if instance.parent else None
#         # representation['children'] = instance.children.__str__()
#         return representation


class IndividualSerializer(serializers.ModelSerializer):
    #timezone сериализуем  в формате JSON
    timezone = TimeZoneSerializerField()

    class Meta:
        model = Individual
        fields = '__all__'

    # отображение значения d get_display()
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['type'] = instance.get_type_display()
        representation['male'] = instance.get_male_display()
        return representation
