from rest_framework import viewsets
from account.serializers import *


class EntityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class IndividualViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
